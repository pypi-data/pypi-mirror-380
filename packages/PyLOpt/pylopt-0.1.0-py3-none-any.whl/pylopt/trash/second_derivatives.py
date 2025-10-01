import torch

def cube_forward(x, a):
    return a * x**3

def cube_backward(grad_out, x, a):
    return grad_out * 3 * a * x**2

def cube_backward_backward(grad_out, sav_grad_out, x, a):
    return grad_out * sav_grad_out * 6 * a * x

def cube_backward_backward_grad_out(grad_out, x, a):
    return grad_out * 3 * a * x**2

class Cube(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x)
        return cube_forward(x, torch.ones(1))

    @staticmethod
    def backward(ctx, grad_out):
        x, = ctx.saved_tensors
        return CubeBackward.apply(grad_out, x)

class CubeBackward(torch.autograd.Function):
    @staticmethod
    def forward(ctx, grad_out, x):
        ctx.save_for_backward(x, grad_out)
        return cube_backward(grad_out, x, torch.ones(1))

    @staticmethod
    def backward(ctx, grad_out):
        x, sav_grad_out = ctx.saved_tensors
        dx = cube_backward_backward(grad_out, sav_grad_out, x, torch.ones(1))
        dgrad_out = cube_backward_backward_grad_out(grad_out, x, torch.ones(1))
        return dgrad_out, dx

class ParamCube(torch.autograd.Function):
    @staticmethod
    def forward(ctx, a, x):
        ctx.save_for_backward(x, a)
        return cube_forward(x, a)

    @staticmethod
    def backward(ctx, grad_out):
        x, a = ctx.saved_tensors
        return None, ParamCubeBackward.apply(grad_out, a, x)

class ParamCubeBackward(torch.autograd.Function):
    @staticmethod
    def forward(ctx, grad_out, a, x):
        ctx.save_for_backward(x, a, grad_out)
        return cube_backward(grad_out, x, a)

    @staticmethod
    def backward(ctx, grad_out):
        x, a, sav_grad_out = ctx.saved_tensors
        dx = cube_backward_backward(grad_out, sav_grad_out, x, a)
        dgrad_out = cube_backward_backward_grad_out(grad_out, x, a)
        return None, dgrad_out, dx

def main():
    x = torch.tensor(1., requires_grad=True)
    a = -torch.ones(1)

    with torch.enable_grad():
        y = Cube.apply(x)
        dy_dx = torch.autograd.grad(inputs=x, outputs=y, create_graph=True)
    d2y_d2x =  torch.autograd.grad(inputs=x, outputs=dy_dx, create_graph=True)

    print('########################################################################')

    with torch.enable_grad():
        y = ParamCube.apply(x, a)
        dy_dx = torch.autograd.grad(inputs=x, outputs=y, create_graph=True)
    d2y_d2x =  torch.autograd.grad(inputs=x, outputs=dy_dx, create_graph=True)

    print(y)
    print(dy_dx)
    print(d2y_d2x)

if __name__ == '__main__':


    main()

# torch.autograd.gradcheck(Cube.apply, x)
# torch.autograd.gradgradcheck(Cube.apply, x)