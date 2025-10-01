from typing import Any, Tuple
import torch
from matplotlib import pyplot as plt
import numpy as np

from bilevel_optimisation.utils.Timer import Timer
#
# SUPP_LOWER = -2.5
# SUPP_UPPER = 2.5
# NUM_NODES = 6

def forward_func(x_scaled, coeffs, weights):
    y = (coeffs[..., 0]
         + x_scaled * (coeffs[..., 1]
                       + x_scaled * (coeffs[..., 2] +
                                     x_scaled * (coeffs[..., 3] + x_scaled * coeffs[..., 4]))))
    # return torch.sum(y * weights, dim=2)
    # out = (y * w).sum(dim=2)
    # return torch.einsum('bfnhw, n->bfhw', y, weights)
    return y * weights.view(1, 1, -1, 1, 1)

def backward_func(x_scaled, b, c, d, e, weights):
    y = (b + x_scaled * (2 * c + x_scaled * (3 * d + x_scaled * 4 * e)))
    return y * weights.view(1, 1, -1, 1, 1)
    # return torch.einsum('bfnhw, n->bfhw', y, weights)

class QuarticBSplineFunction(torch.autograd.Function):

    # @staticmethod
    # def _bucketise(x):
    #     x_scaled = ((x - SUPP_LOWER) /
    #                 (SUPP_UPPER - SUPP_LOWER))
    #     return torch.clamp((x_scaled * (NUM_NODES - 1)).ceil().long(),
    #                        min=0, max=NUM_NODES)

    @staticmethod
    def forward(x_scaled, scale, coeffs, weights) -> Any:
        # x_scaled = x.unsqueeze(dim=2)
        # x_scaled = (x_scaled - centers) / scale
        # index_tensor = QuarticBSplineFunction._bucketise(x_scaled)
        #
        # coeffs_indexed = coeffs[index_tensor]


        # b = coeffs[..., 1]
        # c = coeffs[..., 2]
        # d = coeffs[..., 3]
        # e = coeffs[..., 4]
        #
        # y = (coeffs[..., 0]
        #      + x_scaled * (b
        #                    + x_scaled * (c +
        #                                  x_scaled * (d + x_scaled * e))))
        #
        # return torch.einsum('bfnhw, n->bfhw', y, weights), b, c, d, e
        return forward_func(x_scaled, coeffs, weights), coeffs[..., 1], coeffs[..., 2], coeffs[..., 3], coeffs[..., 4]

    @staticmethod
    def setup_context(ctx: torch.autograd.function.FunctionCtx, inputs: Tuple, outputs: Tuple):
        x_scaled, scale, _, weights = inputs
        _, b, c, d, e = outputs
        ctx.save_for_backward(x_scaled, weights, b, c, d, e)
        ctx.scale = scale

    @staticmethod
    def backward(ctx: torch.autograd.function.FunctionCtx, *grad_outputs: Any) -> Any:
        x_scaled, weights, b, c, d, e = ctx.saved_tensors
        scale = ctx.scale

        # y = (b + x_scaled * (2 * c + x_scaled * (3 * d + x_scaled * 4 * e)))
        y = backward_func(x_scaled, b, c, d, e, weights / scale)
        return grad_outputs[0] * y, *[None] * 3
        # return grad_outputs[0] * torch.sum(y * weights / scale, dim=2), *[None] * 4

class QuarticBSplinePotential(torch.nn.Module):

    SUPP_LOWER = -2.5
    SUPP_UPPER = 2.5
    NUM_NODES = 6

    def __init__(self):
        super().__init__()

        coeffs = torch.zeros(7, 5)
        coeffs[1, :] = torch.tensor([625 / 16, 125 / 2, 75 / 2, 10.0, 1.0]) / 24
        coeffs[2, :] = torch.tensor([55 / 4, -5.0, -30.0, -20.0, -4.0]) / 24.0
        coeffs[3, :] = torch.tensor([115 / 8, 0.0, -15.0, 0.0, 6]) / 24.0
        coeffs[4, :] = torch.tensor([55 / 4, 5.0, -30.0, 20.0, -4.0]) / 24.0
        coeffs[5, :] = torch.tensor([625 / 16, -125 / 2, 75 / 2, -10.0, 1.0]) / 24
        self.register_buffer('coeffs', coeffs)

        box_lower = -3
        box_upper = 3
        num_centers = 33

        centers = torch.linspace(box_lower, box_upper, num_centers)
        self.register_buffer('centers', centers.view(1, 1, -1, 1, 1))
        self.weights = torch.nn.Parameter(torch.log(1 + centers ** 2), requires_grad=True)

        self.scale = (box_upper - box_lower) / (num_centers - 1)

    @classmethod
    def _bucketise(cls, x):
        x_scaled = (x - cls.SUPP_LOWER) / (cls.SUPP_UPPER - cls.SUPP_LOWER)
        return torch.clamp((x_scaled * (cls.NUM_NODES - 1)).ceil().long(), min=0, max=cls.NUM_NODES)

    def forward_(self, x: torch.Tensor, reduce: bool=True) -> torch.Tensor:

        x_scaled = x.unsqueeze(dim=2)
        x_scaled = (x_scaled - self.centers) / self.scale
        index_tensor = self._bucketise(x_scaled)

        coeffs = self.coeffs[index_tensor]

        y = (coeffs[..., 0]
             + x_scaled * (coeffs[..., 1]
                           + x_scaled * (coeffs[..., 2] +
                                         x_scaled * (coeffs[..., 3] + x_scaled * coeffs[..., 4]))))

        y = torch.einsum('bfnhw, n->bfhw', y, self.weights)
        return torch.sum(y) if reduce else y

    def forward(self, x: torch.Tensor, reduce: bool=True) -> torch.Tensor:
        x_scaled = x.unsqueeze(dim=2)
        x_scaled = (x_scaled - self.centers) / self.scale
        index_tensor = self._bucketise(x_scaled)

        coeffs = self.coeffs[index_tensor]

        # y = (coeffs[..., 0]
        #      + x_scaled * (coeffs[..., 1]
        #                    + x_scaled * (coeffs[..., 2] +
        #                                  x_scaled * (coeffs[..., 3] + x_scaled * coeffs[..., 4]))))
        #
        # y = torch.einsum('bfnhw, n->bfhw', y, self.weights)


        y, *_ = QuarticBSplineFunction.apply(x_scaled, self.scale, coeffs, self.weights)


        return torch.sum(y) if reduce else torch.sum(y, dim=(2))


def main():
    device = torch.device('cuda:0')

    pot = QuarticBSplinePotential().to(device=device)

    x = torch.rand(10, 48, 25, 25, device=device, requires_grad=True).to(device=device)
    y = pot(x)
    # y_ = pot.forward_(x)
    # dy_dx = torch.autograd.grad(inputs=x, outputs=y)
    # dy_dx_ = torch.autograd.grad(inputs=x, outputs=y_)

    # pot = torch.compile(pot, mode='max-autotune', backend='inductor', dynamic=True, fullgraph=True)
    #
    # num_predictions = 1000
    # x = torch.rand(10, 48, 256, 256, device=device, requires_grad=True).to(device=device)
    #
    # # profile(pot, device, True)
    #
    # timings = []
    # for _ in range(0, num_predictions):
    #     with Timer(device) as t:
    #         y = pot(x)
    #         with torch.no_grad():
    #             dy_dx = torch.autograd.grad(inputs=x, outputs=y)
    #
    #     timings.append(t.time_delta())
    #
    # print('median: {:.5f}'.format(np.median(timings)))
    # print('mean: {:.5f}'.format(np.mean(timings)))
    # print('mean (tail): {:.5f}'.format(np.mean(timings[5::])))

    t = torch.stack([torch.linspace(-2, 2, 111)
                     for _ in range(0, 48)]).unsqueeze(dim=1).unsqueeze(dim=0).requires_grad_(True).to(device=device)

    p = pot(t, reduce=False)

    fig = plt.figure()
    ax_1 = fig.add_subplot(3, 1, 1)
    ax_2 = fig.add_subplot(3, 1, 2)
    ax_3 = fig.add_subplot(3, 1, 3)


    ax_1.plot(t[0, 0, 0, :].detach().cpu().numpy(), p[0, 0, 0, :].detach().cpu().numpy(), color='orange')
    ax_2.plot(t[0, 0, 0, :].detach().cpu().numpy(), p[0, 1, 0, :].detach().cpu().numpy(), color='orange')
    ax_3.plot(t[0, 0, 0, :].detach().cpu().numpy(), p[0, 2, 0, :].detach().cpu().numpy(), color='orange')
    plt.show()

def b_splines():



    x = torch.linspace(0.0, 1.0, 3000)

    nodes = torch.tensor([0.0, 0.25, 0.5, 0.75, 1.0])
    l = len(nodes) - 2
    kk = 4
    n = l + kk
    print(n)

    nodes_extended = torch.cat([nodes[0] * torch.ones(kk - 1), nodes, nodes[-1] * torch.ones(kk - 1)])
    basis = torch.zeros((len(x), len(nodes_extended) - 1))

    # if kk == 1:
    #     for j in range(0, n - k):
    #         basis[:, j] = (x >= nodes_extended[j]) & (x < nodes_extended[j + 1])

    if kk >= 2:
        delta = 0.25
        k = 1
        # for j in range(0, len(nodes_extended) - k - 1 - 1):
        for j in range(0, len(nodes_extended) - k):
            basis[:, j] = (x >= nodes_extended[j]) & (x < nodes_extended[j + 1])

        y = x.reshape(-1, 1) - nodes_extended.reshape(1, -1)

        k = 2
        for j in range(0, len(nodes_extended) - k):
            if nodes_extended[j] == nodes_extended[j + k - 1]:
                left = 0.0
            else:
                left = ((x - nodes_extended[j]) / (nodes_extended[j + k - 1] - nodes_extended[j])) * basis[:, j]

            if nodes_extended[j + 1] == nodes_extended[j + k]:
                right = 0.0
            else:
                right = ((nodes_extended[j + k] - x) / (nodes_extended[j + k] - nodes_extended[j + 1])) * basis[:, j + 1]
            basis[:, j] = left + right

        k = 3
        for j in range(0, len(nodes_extended) - k):
            if nodes_extended[j] == nodes_extended[j + k - 1]:
                left = 0.0
            else:
                left = ((x - nodes_extended[j]) / (nodes_extended[j + k - 1] - nodes_extended[j])) * basis[:, j]

            if nodes_extended[j + 1] == nodes_extended[j + k]:
                right = 0.0
            else:
                right = ((nodes_extended[j + k] - x) / (nodes_extended[j + k] - nodes_extended[j + 1])) * basis[:, j + 1]
            basis[:, j] = left + right

        k = 4
        for j in range(0, len(nodes_extended) - k):
            if nodes_extended[j] == nodes_extended[j + k - 1]:
                left = 0.0
            else:
                left = ((x - nodes_extended[j]) / (nodes_extended[j + k - 1] - nodes_extended[j])) * basis[:, j]

            if nodes_extended[j + 1] == nodes_extended[j + k]:
                right = 0.0
            else:
                right = ((nodes_extended[j + k] - x) / (nodes_extended[j + k] - nodes_extended[j + 1])) * basis[:, j + 1]
            basis[:, j] = left + right

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for j in range(0, n):
        ax.plot(x, basis[:, j])

    plt.show()

def profile(model, device, gradients):
    x = torch.rand(10, 48, 256, 256, device=device, requires_grad=gradients)

    with torch.profiler.profile() as prof:
        y = model(x)
        if gradients:
            dy_dx = torch.autograd.grad(inputs=x, outputs=torch.sum(y))

    with torch.profiler.profile() as prof:
        y = model(x)
        if gradients:
            dy_dx = torch.autograd.grad(inputs=x, outputs=torch.sum(y))

    print(prof.key_averages().table())

if __name__ == '__main__':
    main()
    # b_splines()
