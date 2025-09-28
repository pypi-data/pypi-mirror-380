import torch
from ...core import Transform

from ...utils.derivatives import jacobian_wrt, flatten_jacobian
from ...utils import vec_to_tensors
from ...linalg import linear_operator
from .lmadagrad import lm_adagrad_apply, lm_adagrad_update

class NaturalGradient(Transform):
    """Natural gradient approximated via empirical fisher information matrix.

    To use this, either pass vector of per-sample losses to the step method, or make sure
    the closure returns it. Gradients will be calculated via batched autograd within this module,
    you don't need to implement the backward pass. When using closure, please add the ``backward`` argument,
    it will always be False but it is required. See below for an example.

    Note:
        Empirical fisher information matrix may give a really bad approximation in some cases.
        If that is the case, set ``sqrt`` to True to perform whitening instead, which is way more robust.

    Args:
        reg (float, optional): regularization parameter. Defaults to 1e-8.
        sqrt (bool, optional):
            if True, uses square root of empirical fisher information matrix. Both EFIM and it's square
            root can be calculated and stored efficiently without ndim^2 memory. Square root
            whitens the gradient and often performs much better, especially when you try to use NGD
            with a vector that isn't strictly per-sample gradients, but rather for example different losses.
        gn_grad (bool, optional):
            if True, uses Gauss-Newton G^T @ f as the gradient, which is effectively sum weighted by value
            and is equivalent to squaring the values. That makes the kernel trick solver incorrect, but for
            some reason it still works. If False, uses sum of per-sample gradients.
            This has an effect when ``sqrt=False``, and affects the ``grad`` attribute.
            Defaults to False.
        batched (bool, optional): whether to use vmapping. Defaults to True.

    Examples:

    training a neural network:
    ```python
    X = torch.randn(64, 20)
    y = torch.randn(64, 10)

    model = nn.Sequential(nn.Linear(20, 64), nn.ELU(), nn.Linear(64, 10))
    opt = tz.Modular(
        model.parameters(),
        tz.m.NaturalGradient(),
        tz.m.LR(3e-2)
    )

    for i in range(100):
        y_hat = model(X) # (64, 10)
        losses = (y_hat - y).pow(2).mean(0) # (10, )
        opt.step(loss=losses)
        if i % 10 == 0:
            print(f'{losses.mean() = }')
    ```

    training a neural network - closure version
    ```python
    X = torch.randn(64, 20)
    y = torch.randn(64, 10)

    model = nn.Sequential(nn.Linear(20, 64), nn.ELU(), nn.Linear(64, 10))
    opt = tz.Modular(
        model.parameters(),
        tz.m.NaturalGradient(),
        tz.m.LR(3e-2)
    )

    def closure(backward=True):
        y_hat = model(X) # (64, 10)
        return (y_hat - y).pow(2).mean(0) # (10, )

    for i in range(100):
        losses = opt.step(closure)
        if i % 10 == 0:
        print(f'{losses.mean() = }')
    ```

    minimizing the rosenbrock function with a mix of natural gradient, whitening and gauss-newton:
    ```python
    def rosenbrock(X):
        x1, x2 = X
        return torch.stack([(1 - x1).abs(), (10 * (x2 - x1**2).abs())])

    X = torch.tensor([-1.1, 2.5], requires_grad=True)
    opt = tz.Modular([X], tz.m.NaturalGradient(sqrt=True, gn_grad=True), tz.m.LR(0.05))

    for iter in range(200):
        losses = rosenbrock(X)
        opt.step(loss=losses)
        if iter % 20 == 0:
            print(f'{losses.mean() = }')
    ```
    """
    def __init__(self, reg:float = 1e-8, sqrt:bool=False, gn_grad:bool=False, batched:bool=True, ):
        super().__init__(defaults=dict(batched=batched, reg=reg, sqrt=sqrt, gn_grad=gn_grad))

    @torch.no_grad
    def update_states(self, objective, states, settings):
        params = objective.params
        fs = settings[0]
        batched = fs['batched']
        gn_grad = fs['gn_grad']

        closure = objective.closure
        assert closure is not None

        with torch.enable_grad():
            f = objective.get_loss(backward=False) # n_out
            assert isinstance(f, torch.Tensor)
            G_list = jacobian_wrt([f.ravel()], params, batched=batched)

        objective.loss = f.sum()
        G = self.global_state["G"] = flatten_jacobian(G_list) # (n_samples, ndim)

        if gn_grad:
            g = self.global_state["g"] = G.H @ f.detach()

        else:
            g = self.global_state["g"] = G.sum(0)

        objective.grads = vec_to_tensors(g, params)

        # set closure to calculate scalar value for line searches etc
        if objective.closure is not None:
            def ngd_closure(backward=True):
                if backward:
                    objective.zero_grad()
                    with torch.enable_grad():
                        loss = closure(False)
                        if gn_grad: loss = loss.pow(2)
                        loss = loss.sum()
                        loss.backward()
                    return loss

                loss = closure(False)
                if gn_grad: loss = loss.pow(2)
                return loss.sum()

            objective.closure = ngd_closure

    @torch.no_grad
    def apply_states(self, objective, states, settings):
        params = objective.params
        fs = settings[0]
        reg = fs['reg']
        sqrt = fs['sqrt']

        G: torch.Tensor = self.global_state['G'] # (n_samples, n_dim)

        if sqrt:
            # this computes U, S <- SVD(M), then calculate update as U S^-1 Uᵀg,
            # but it computes it through eigendecompotision
            U, L = lm_adagrad_update(G.H, reg, 0)
            if U is None or L is None: return objective

            v = lm_adagrad_apply(self.global_state["g"], U, L)
            objective.updates = vec_to_tensors(v, params)
            return objective

        # we need (G^T G)v = g
        # where g = G^T
        # so we need to solve (G^T G)v = G^T
        GGT = G @ G.H # (n_samples, n_samples)

        if reg != 0:
            GGT.add_(torch.eye(GGT.size(0), device=GGT.device, dtype=GGT.dtype).mul_(reg))

        z, _ = torch.linalg.solve_ex(GGT, torch.ones_like(GGT[0])) # pylint:disable=not-callable
        v = G.H @ z

        objective.updates = vec_to_tensors(v, params)
        return objective


    def get_H(self, objective=...):
        if "G" not in self.global_state: return linear_operator.ScaledIdentity()
        G = self.global_state['G']
        return linear_operator.AtA(G)
