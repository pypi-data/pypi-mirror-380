from typing import Any, Tuple

import torch

def cube_forward(x):
    return x**3

def cube_backward(grad_out, x):
    return grad_out * 3 * x**2

def cube_backward_backward(grad_out, sav_grad_out, x):
    return grad_out * sav_grad_out * 6 * x

def cube_backward_backward_grad_out(grad_out, x):
    return grad_out * 3 * x**2

class Cube(torch.autograd.Function):
    @staticmethod
    def forward(x, s='grrrrrr'):
        t = 'asd'
        return cube_forward(x), t

    @staticmethod
    def setup_context(ctx: Any, inputs: Tuple[Any, ...], output: Any) -> Any:
        x, s = inputs
        _, t = output
        ctx.save_for_backward(x)
        ctx.s = s
        ctx.t = t

    @staticmethod
    def backward(ctx, *grad_out):
        x, = ctx.saved_tensors
        s = ctx.s
        return CubeBackward.apply(grad_out[0], x), None

class CubeBackward(torch.autograd.Function):
    @staticmethod
    def forward(grad_out, x):
        return cube_backward(grad_out, x)

    @staticmethod
    def setup_context(ctx: Any, inputs: Tuple[Any, ...], output: Any) -> Any:
        grad_out, x = inputs
        ctx.save_for_backward(x)
        ctx.grad_out = grad_out

    @staticmethod
    def backward(ctx, *grad_out):
        x, = ctx.saved_tensors
        sav_grad_out = ctx.grad_out
        dx = cube_backward_backward(grad_out[0], sav_grad_out, x)
        dgrad_out = cube_backward_backward_grad_out(grad_out[0], x)
        return dgrad_out, dx


x = torch.tensor(3., requires_grad=True, dtype=torch.double)

with torch.enable_grad():
    y = Cube.apply(x, 'bla')[0]
    dy_dx = torch.autograd.grad(inputs=x, outputs=y, create_graph=True)[0].requires_grad_(True)
print(dy_dx)
print(dy_dx.requires_grad)

v = torch.tensor(-6.66)
d2y_dx2 = torch.autograd.grad(inputs=x, outputs=dy_dx, grad_outputs=v)

print('asd')

def func(z):
    return Cube.apply(z, 'yippie')[0]

torch.autograd.gradcheck(func, (x,))
torch.autograd.gradgradcheck(func, (x, ))