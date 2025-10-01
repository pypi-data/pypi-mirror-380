from typing import Any, Tuple, Optional
import numpy as np
import torch
from torch.autograd import Function
from torch.autograd.function import FunctionCtx
from contextlib import nullcontext

from bilevel_optimisation.solver.solve_tridiagonal import solve_tridiagonal
from bilevel_optimisation.utils.Timer import Timer

def spline_forward(x, a, b, c, d):
    return a + x * (b + x * (c + x * d))

def first_order_spline_derivative(x, b, c, d):
    return b + x * (2 * c + 3 * d * x)

def second_order_spline_derivative(x, c, d):
    return 2 * c + 6 * d * x

class SplineBackward(Function):
    @staticmethod
    def bucketise(x: torch.Tensor, box_lower, box_upper, num_nodes):
        x_scaled = (x - box_lower) / (box_upper - box_lower)
        return torch.clamp((x_scaled * (num_nodes - 1)).ceil().long() - 1, min=0, max=num_nodes - 2)

    @staticmethod
    def compute_nodal_grad(grad_out, x, nodal_values, nodes, num_marginals, step_size, box_lower, box_upper, num_nodes):
        index_tensor = SplineBackward.bucketise(x, box_lower, box_upper, num_nodes)
        y = x - nodes[index_tensor]

        bs, f, w, h = x.shape
        idx_flat = index_tensor.view(bs, f, w, h).permute(1, 0, 2, 3).reshape(f, -1)

        nodals = nodal_values.detach().clone().requires_grad_(True)
        with torch.enable_grad():
            nodals, coeffs_1st_order, coeffs_2nd_order, coeffs_3rd_order = NaturalCubicSpline.nodal_values_to_coefficients(nodals, num_nodes, num_marginals, step_size)

            a = nodals.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
            b = coeffs_1st_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
            c = coeffs_2nd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
            d = coeffs_3rd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)

            spline_pot = torch.sum(spline_forward(y, a, b, c, d))
        grad_nodal = torch.autograd.grad(inputs=nodals, outputs=spline_pot)[0]
        return grad_out * grad_nodal, b, c, d, y

    @staticmethod
    def forward(x, nodal_values, nodes, num_marginals, step_size, box_lower, box_upper, num_nodes) -> Tuple[torch.Tensor, ...]:
        index_tensor = SplineBackward.bucketise(x, box_lower, box_upper, num_nodes)
        y = x - nodes[index_tensor]

        bs, f, w, h = x.shape
        idx_flat = index_tensor.view(bs, f, w, h).permute(1, 0, 2, 3).reshape(f, -1)

        # nodals = nodal_values.detach().clone().requires_grad_(True)
        # with torch.enable_grad():
        nodals, coeffs_1st_order, coeffs_2nd_order, coeffs_3rd_order = (
            NaturalCubicSpline.nodal_values_to_coefficients(nodal_values, num_nodes, num_marginals, step_size))

        a = nodals.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
        b = coeffs_1st_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
        c = coeffs_2nd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
        d = coeffs_3rd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)

        #     spline_pot = torch.sum(spline_forward(y, a, b, c, d))
        #     grad_nodal = torch.autograd.grad(inputs=nodals, outputs=spline_pot, create_graph=True)[0]

        return torch.sum(spline_forward(y, a, b, c, d)), a, b, c, d

    @staticmethod
    def setup_context(ctx: Any, inputs: Tuple[Any, ...], output: Tuple[torch.Tensor, ...]) -> Any:
        # x = inputs[0]
        # nodal_values = inputs[1]
        # nodes = inputs[2]
        x, nodal_values, nodes, num_marginals, step_size, box_lower, box_upper, num_nodes = inputs

        ctx.save_for_backward(x, nodal_values, nodes)
        ctx.num_marginals = num_marginals
        ctx.step_size = step_size
        ctx.box_lower = box_lower
        ctx.box_upper = box_upper
        ctx.num_nodes = num_nodes

    @staticmethod
    def backward(ctx: Any, *grad_outputs: Any) -> Any:
        x, nodal_values, nodes = ctx.saved_tensors
        num_marginals = ctx.num_marginals
        step_size = ctx.step_size
        box_lower = ctx.box_lower
        box_upper = ctx.box_upper
        num_nodes = ctx.num_nodes
        return SplineBackwardBackward.apply(grad_outputs[0], x, nodal_values, nodes, num_marginals, step_size, box_lower, box_upper, num_nodes)

class SplineBackwardBackward(Function):
    @staticmethod
    def forward(grad_out, x, nodal_values, nodes, num_marginals, step_size, box_lower, box_upper, num_nodes) -> Any:
        grad_nodal, b, c, d, y = SplineBackward.compute_nodal_grad(grad_out, x, nodal_values, nodes, num_marginals, step_size,
                                                       box_lower, box_upper, num_nodes)

        grad_x = grad_out * first_order_spline_derivative(y, b, c, d)

        return grad_x, grad_out * grad_nodal, *[None] * 6

    @staticmethod
    def setup_context(ctx: Any, inputs: Tuple[Any, ...], output: Any) -> Any:
        grad_out, x, _, a, b, c, d, y, _ = inputs
        ctx.save_for_backward(a, b, c, d, y)
        ctx.grad_out = grad_out

    @staticmethod
    def backward(ctx: Any, *grad_outputs: Any) -> Any:
        a, b, c, d, y = ctx.saved_tensors
        grad_out = ctx.grad_out

        partial_x = grad_outputs[0]
        partial_nodals = grad_outputs[1]

        summand_1 = grad_out * second_order_spline_derivative(y, c, d) * partial_x

        summand_2 = grad_out * ... * partial_nodals
        grad_dx_dx = summand_1 + summand_2

        grad_dx_dnodals

        dx = grad_out * grad_outputs[0] * second_order_spline_derivative(y, c, d)
        dgrad_out = grad_outputs[0] * first_order_spline_derivative(y, b, c, d)

        return dgrad_out, dx, *[None] * 7

# class NaturalSplineAutogradFunction(Function):
#
#     @staticmethod
#     def bucketise(x: torch.Tensor, box_lower, box_upper, num_nodes):
#         x_scaled = (x - box_lower) / (box_upper - box_lower)
#         return torch.clamp((x_scaled * (num_nodes - 1)).ceil().long() - 1, min=0, max=num_nodes - 2)
#
#     @staticmethod
#     def forward(ctx: FunctionCtx, nodes, nodal_values, coeffs_1st_order, coeffs_2nd_order,
#                 coeffs_3rd_order, box_lower, box_upper, num_nodes, x,
#                 grad_outputs=None, order=0) -> Tuple[torch.Tensor, Optional[Any]]:
#         index_tensor = NaturalSplineAutogradFunction.bucketise(x, box_lower, box_upper, num_nodes)
#         y = x - nodes[index_tensor]
#
#         bs, f, w, h = x.shape
#         idx_flat = index_tensor.view(bs, f, w, h).permute(1, 0, 2, 3).reshape(f, -1)
#
#         context = torch.enable_grad() if order == 2 else nullcontext()
#         with context:
#             a = nodal_values.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
#             b = coeffs_1st_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
#             c = coeffs_2nd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
#             d = coeffs_3rd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
#
#             ds_dx = first_order_spline_derivative(y, b, c, d)
#
#         ctx.save_for_backward(y, b, c, d)
#         ctx.order = order
#
#         if order == 0:
#             return a + y * (b + y * (c + y * d)), None
#         elif order == 1:
#             return first_order_spline_derivative(y, b, c, d), None
#         elif order == 2:
#             grad_outputs = torch.ones_like(y) if grad_outputs is None else grad_outputs
#             d2s_mixed = torch.autograd.grad(inputs=nodal_values, outputs=ds_dx, grad_outputs=grad_outputs)
#             return second_order_spline_derivative(y, c, d), d2s_mixed
#         else:
#             raise ValueError
#
#     @staticmethod
#     def backward(ctx: FunctionCtx, *grad_outputs: Any) -> Any:
#         y, b, c, d = ctx.saved_tensors
#         order = ctx.order
#
#         grad = None
#         if order == 0:
#             grad = grad_outputs * first_order_spline_derivative(y, b, c, d)
#         elif order == 1:
#             grad = grad_outputs * second_order_spline_derivative(y, c, d)
#         else:
#             print('problem: nix gut!')
#
#         return *[None] * 8, grad, None, None



class NaturalCubicSplinePotential(torch.nn.Module):

    def __init__(self, num_marginals: int, num_nodes: int, box_lower: float, box_upper: float) -> None:

        super().__init__()
        self.num_marginals = num_marginals

        self.num_nodes = num_nodes
        self.box_lower = box_lower
        self.box_upper = box_upper
        self.register_buffer('nodes', torch.linspace(self.box_lower, self.box_upper, self.num_nodes))
        self.step_size = self.nodes[1] - self.nodes[0]

        vals_1 = torch.tensor([5.0, 2.0, 4.0])
        vals_2 = torch.tensor([-3.0, -2.0, -1.0])
        vals = torch.stack([vals_1, vals_2]).to(device=torch.device('cuda'))

        self.nodal_values = torch.nn.Parameter(vals, requires_grad=True)

    def forward_(self, x):

        index_tensor = SplineBackward.bucketise(x, self.box_lower, self.box_upper, self.num_nodes)

        y = x - self.nodes[index_tensor]

        bs, f, w, h = x.shape
        idx_flat = index_tensor.view(bs, f, w, h).permute(1, 0, 2, 3).reshape(f, -1)

        nodals, coeffs_1st_order, coeffs_2nd_order, coeffs_3rd_order = (
            NaturalCubicSpline.nodal_values_to_coefficients(self.nodal_values, self.num_nodes, self.num_marginals, self.step_size))

        a = nodals.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
        b = coeffs_1st_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
        c = coeffs_2nd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)
        d = coeffs_3rd_order.gather(1, idx_flat).view(f, bs, w, h).permute(1, 0, 2, 3)


        return torch.sum(spline_forward(y, a, b, c, d))

    def forward(self, x):
        return SplineBackward.apply(x, self.nodal_values, self.nodes, self.num_marginals,
                              self.step_size, self.box_lower, self.box_upper, self.num_nodes)[0]



class NaturalCubicSpline(torch.nn.Module):

    def __init__(self, num_marginals: int, num_nodes: int, box_lower: float, box_upper: float) -> None:
        super().__init__()

        self.num_marginals = num_marginals

        self.num_nodes = num_nodes
        self.box_lower = box_lower
        self.box_upper = box_upper
        self.register_buffer('nodes', torch.linspace(self.box_lower, self.box_upper, self.num_nodes))
        self.step_size = self.nodes[1] - self.nodes[0]

        vals_1 = torch.tensor([5.0, 2.0, 4.0])
        vals_2 = torch.tensor([-3.0, -2.0, -1.0])
        vals = torch.stack([vals_1, vals_2]).to(device=torch.device('cuda'))
        # vals = torch.rand(num_marginals, num_nodes, device=torch.device('cuda'))
        # vals = torch.stack([torch.log(1 + self.nodes ** 2), torch.log(1 + self.nodes ** 2)])

        self.nodal_values = torch.nn.Parameter(vals, requires_grad=True)

        self.diag = torch.ones(self.num_nodes, device=torch.device('cuda'))
        self.diag[1:-1] = 4
        self.diag_super = torch.ones(self.num_nodes - 1, device=torch.device('cuda'))
        self.diag_super[0] = 0
        self.diag_sub = torch.ones(self.num_nodes - 1, device=torch.device('cuda'))
        self.diag_sub[-1] = 0

        self.coeffs_1st_order = torch.zeros(self.num_marginals, self.num_nodes - 1, device=torch.device('cuda'))
        self.coeffs_2nd_order = torch.zeros(self.num_marginals, self.num_nodes - 1, device=torch.device('cuda'))
        self.coeffs_3rd_order = torch.zeros(self.num_marginals, self.num_nodes - 1, device=torch.device('cuda'))

        self._interpolate()

    @staticmethod
    def nodal_values_to_coefficients(nodal_values, num_nodes, num_marginals, step_size):

        diag = torch.ones(num_nodes, device=torch.device('cuda'))
        diag[1:-1] = 4
        diag_super = torch.ones(num_nodes - 1, device=torch.device('cuda'))
        diag_super[0] = 0
        diag_sub = torch.ones(num_nodes - 1, device=torch.device('cuda'))
        diag_sub[-1] = 0

        rhs = torch.zeros(num_marginals, num_nodes, device=torch.device('cuda'))
        rhs[:, 1 : num_nodes - 1] = 3 * (nodal_values[:, 0 : num_nodes - 2] -
                                              2 * nodal_values[:, 1 : num_nodes - 1] +
                                              nodal_values[:, 2::]) / (step_size ** 2)

        coeffs_2nd_order = solve_tridiagonal(diag, diag_super, diag_sub, rhs)
        coeffs_1st_order = ((nodal_values[:, 1 ::] - nodal_values[:, 0 : -1]) / step_size -
                                      step_size * (2 * coeffs_2nd_order[:, 0 : -1] +
                                                        coeffs_2nd_order[:, 1 ::]) / 3)
        coeffs_3rd_order = (coeffs_2nd_order[:, 1 ::] - coeffs_2nd_order[:, 0 : -1]) / (3 * step_size)

        return nodal_values, coeffs_1st_order, coeffs_2nd_order, coeffs_3rd_order

    def _interpolate(self) -> None:
        rhs = torch.zeros(self.num_marginals, self.num_nodes, device=torch.device('cuda'))
        rhs[:, 1 : self.num_nodes - 1] = 3 * (self.nodal_values[:, 0 : self.num_nodes - 2] -
                                              2 * self.nodal_values[:, 1 : self.num_nodes - 1] +
                                              self.nodal_values[:, 2::]) / (self.step_size ** 2)

        self.coeffs_2nd_order = solve_tridiagonal(self.diag, self.diag_super, self.diag_sub, rhs)
        self.coeffs_1st_order = ((self.nodal_values[:, 1 ::] - self.nodal_values[:, 0 : -1]) / self.step_size -
                                      self.step_size * (2 * self.coeffs_2nd_order[:, 0 : -1] +
                                                        self.coeffs_2nd_order[:, 1 ::]) / 3)
        self.coeffs_3rd_order = (self.coeffs_2nd_order[:, 1 ::] - self.coeffs_2nd_order[:, 0 : -1]) / (3 * self.step_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return SplineBackward.apply(x, self.nodal_values, self.nodes, self.num_marginals,
                                    self.step_size, self.box_lower, self.box_upper, self.num_nodes)[0]

        # return NaturalSplineAutogradFunction.apply(self.nodes, self.nodal_values, self.coeffs_1st_order,
        #                                     self.coeffs_2nd_order, self.coeffs_3rd_order,
        #                                     self.box_lower, self.box_upper, self.num_nodes, x)[0]

    def first_derivative(self, x) -> torch.Tensor:
        # return NaturalSplineAutogradFunction.apply(self.nodes, self.nodal_values, self.coeffs_1st_order,
        #                                     self.coeffs_2nd_order, self.coeffs_3rd_order,
        #                                     self.box_lower, self.box_upper, self.num_nodes, x, None, 1)[0]
        pass


    def second_derivative(self, x) -> torch.Tensor:
        # return NaturalSplineAutogradFunction.apply(self.nodes, self.nodal_values, self.coeffs_1st_order,
        #                                            self.coeffs_2nd_order, self.coeffs_3rd_order,
        #                                            self.box_lower, self.box_upper, self.num_nodes, x, None, 2)
        pass


def example_tridiag():
    d = 4.0 * torch.ones(4).to(dtype=torch.float32)
    d_super = torch.ones(3).to(dtype=torch.float32)
    d_sub = torch.ones(3).to(dtype=torch.float32)

    rhs_1 = torch.arange(0, 4).to(dtype=torch.float32)
    rhs_2 = torch.arange(4, 8).to(dtype=torch.float32)
    rhs = torch.stack([rhs_1, rhs_2]).to(dtype=torch.float32)

    x = solve_tridiagonal(d, d_super, d_sub, rhs)

    A = torch.diag(d) + torch.diag(d_super, diagonal=1) + torch.diag(d_sub, diagonal=-1)

    x_1 = torch.linalg.solve(A, rhs_1)
    x_2 = torch.linalg.solve(A, rhs_2)

    print(x)

    print(x_1)
    print(x_2)

def example_spline():
    spline = NaturalCubicSpline(2, 3, 5, 9)
    spline.to(device=torch.device('cuda'))

    t0 = torch.linspace(5, 9, 111)
    t1 = torch.linspace(5, 9, 111)
    t = torch.stack([t0, t1]).unsqueeze(dim=1).unsqueeze(dim=0).to(device=torch.device('cuda')).requires_grad_(True)

    y = spline(t)
    dy_dt = torch.autograd.grad(inputs=t, outputs=torch.sum(y), create_graph=True)[0]
    d2y_dt2 = torch.autograd.grad(inputs=t, outputs=dy_dt, grad_outputs=torch.ones_like(t))[0]

        # x = torch.ones_like(t).requires_grad_(True)
        # def func(z):
        #     return SplineBackward.apply(x, spline.nodes, spline.nodal_values, spline.coeffs_1st_order,
        #                                 spline.coeffs_2nd_order, spline.coeffs_3rd_order, spline.box_lower,
        #                                 spline.box_upper, spline.num_nodes)[0]
        # torch.autograd.gradcheck(func, (x,))


        # dy_dt = spline.first_derivative(t)
        # d2y_d2t, d2y_mixed = spline.second_derivative(t)


    from matplotlib import pyplot as plt
    fig = plt.figure()
    ax_1 = fig.add_subplot(1, 3, 1)
    ax_1.plot(t0.numpy(), y[0, 0, 0, :].squeeze().cpu().detach().numpy())

    t00 = torch.linspace(5, 7, 55)
    p_0 = 5 - 2.125 * (t00 - 5) + 0.1562 * (t00 - 5) ** 3

    t11 = torch.linspace(7, 9, 55)
    p_1 = 2 - 0.25 * (t11 - 7) + 0.9375 * (t11 - 7) ** 2 - 0.1562 * (t11 - 7) ** 3

    ax_1.plot(t00.numpy(), p_0.squeeze().cpu().detach().numpy(), color='magenta')
    ax_1.plot(t11.numpy(), p_1.squeeze().cpu().detach().numpy(), color='cyan')

    ax_1.plot(t1.numpy(), y[0, 1, 0, :].squeeze().cpu().detach().numpy())



    ax_2 = fig.add_subplot(1, 3, 2)
    ax_2.plot(t0.numpy(), dy_dt[0, 0, 0, :].squeeze().cpu().detach().numpy())
    ax_2.plot(t1.numpy(), dy_dt[0, 1, 0, :].squeeze().cpu().detach().numpy())

    dp_0 =  - 2.125 + 3 * 0.1562 * (t00 - 5) ** 2
    dp_1 = - 0.25 + 2 * 0.9375 * (t11 - 7) - 3 * 0.1562 * (t11 - 7) ** 2

    ax_2.plot(t00.numpy(), dp_0.squeeze().cpu().detach().numpy(), color='magenta')
    ax_2.plot(t11.numpy(), dp_1.squeeze().cpu().detach().numpy(), color='cyan')

    d2p_0 = 6 * 0.1562 * (t00 - 5)
    d2p_1 = 2 * 0.9375 - 6 * 0.1562 * (t11 - 7)

    ax_3 = fig.add_subplot(1, 3, 3)
    ax_3.plot(t0.numpy(), d2y_dt2[0, 0, 0, :].squeeze().cpu().detach().numpy())
    ax_3.plot(t1.numpy(), d2y_dt2[0, 1, 0, :].squeeze().cpu().detach().numpy())
    ax_3.plot(t00.numpy(), d2p_0.squeeze().cpu().detach().numpy(), color='magenta')
    ax_3.plot(t11.numpy(), d2p_1.squeeze().cpu().detach().numpy(), color='cyan')

    plt.show()

def evaluate_spline(num_predictions, device, gradients):

    spline = NaturalCubicSpline(48, 33, 5, 9)
    spline.to(device=torch.device('cuda'))
    spline._interpolate()

    x = torch.rand(10, 48, 256, 256, device=device, requires_grad=gradients)

    spline = torch.compile(spline, mode='max-autotune', backend='inductor', dynamic=True,
								 fullgraph=True)
    #
    #
    timings = []
    for _ in range(0, num_predictions):
        with Timer(device) as t:
            with torch.no_grad():
                y = spline(x)
        timings.append(t.time_delta())

    print('median: {:.5f}'.format(np.median(timings)))
    print('mean: {:.5f}'.format(np.mean(timings)))
    print('mean (tail): {:.5f}'.format(np.mean(timings[5::])))

    print('# ### ##############################################################')

    with torch.no_grad():
        spline.nodal_values.copy_(torch.ones(48, 33, device=torch.device('cuda')))
    spline._interpolate()

    timings = []
    for _ in range(0, 10):
        with Timer(device) as t:
            y = torch.sum(spline(x))
            dy_dx = torch.autograd.grad(inputs=x, outputs=y)
        timings.append(t.time_delta())

    print('median: {:.5f}'.format(np.median(timings)))
    print('mean: {:.5f}'.format(np.mean(timings)))
    print('mean (tail): {:.5f}'.format(np.mean(timings[5::])))

def second_derivative():
    spline = NaturalCubicSpline(2, 3, 5, 9)

    spline._interpolate()
    spline.to(device=torch.device('cuda'))


    t0 = torch.linspace(5, 9, 111)
    t1 = torch.linspace(5, 9, 111)
    t = torch.stack([t0, t1]).unsqueeze(dim=1).unsqueeze(dim=0).to(device=torch.device('cuda')).requires_grad_(True)

    print('# ### ############################################################################')
    print('first derivative')
    with torch.enable_grad():
        y = torch.sum(spline(t))
    dy_dx = torch.autograd.grad(inputs=t, outputs=y)[0]
    dy_dx_ = spline.first_derivative(t)

    print(dy_dx.shape)
    print(torch.linalg.norm(dy_dx - dy_dx_))

    print('# ### ############################################################################')

    dz_dt_ = spline.second_derivative(t)

    with torch.enable_grad():
        z = torch.sum(spline.first_derivative(t))
    dz_dt = torch.autograd.grad(inputs=t, outputs=z)[0]

    print(dz_dt.shape)
    print(torch.linalg.norm(dz_dt - dz_dt_))

    print('# ### ############################################################################')
    with torch.enable_grad():
        y = torch.sum(spline(t))
    dy_dx = torch.autograd.grad(inputs=spline.parameters(), outputs=y)[0]



    # with torch.enable_grad():
    #     y = torch.sum(spline(t))
    #     dy_dx = torch.autograd.grad(inputs=t, outputs=y, create_graph=True)
    # d2y_d2x = torch.autograd.grad(inputs=t, outputs=dy_dx, create_graph=True, grad_outputs=torch.rand_like(t))

class DummyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()



def spline_pot_example():
    pot = NaturalCubicSplinePotential(2, 3, 5, 9)
    pot.to(device=torch.device('cuda'))
    #
    bs = 10
    f = 48
    w = 256
    h = 256
    x = torch.rand(bs, f, w, h).cuda()
    x.requires_grad_(True)
    #
    # y = pot.forward_(x)
    # grad_x = torch.autograd.grad(inputs=x, outputs=y, retain_graph=True, create_graph=True)[0]
    #
    # z = torch.sum(grad_x)
    # dz_dnodal = torch.autograd.grad(inputs=[p for p in pot.parameters() if p.requires_grad], outputs=z)
    #
    # asd

    num_trials = 100

    times_1 = []
    for i in range(0, num_trials):
        with Timer(torch.device('cuda')) as t:
            y = pot(x)
            #grad_x = torch.autograd.grad(inputs=x, outputs=y, retain_graph=True)[0]
        times_1.append(t.time_delta())

    grad_nodals = torch.autograd.grad(inputs=pot.nodal_values, outputs=y)[0]

    x_ = x.detach().clone().requires_grad_(True)
    times_2 = []
    for i in range(0, num_trials):
        with Timer(torch.device('cuda')) as t:
            y_ = pot.forward_(x_)
            #grad_x_ = torch.autograd.grad(inputs=x_, outputs=y_, retain_graph=True)[0]
        times_2.append(t.time_delta())

    print(np.mean(times_1))
    print(np.mean(times_2))

    print(torch.linalg.norm(y - y_))
    # print(torch.linalg.norm(grad_x_ - grad_x))


    print('')


if __name__ == '__main__':
    # example_tridiag()
    example_spline()

    # spline_pot_example()

    evaluate_spline(100, torch.device('cuda'), True)

    # second_derivative()



