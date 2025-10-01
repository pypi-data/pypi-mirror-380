import torch

def poly_func(x):

    a = 3
    b = 2
    c = 1
    d = 4
    return a + x * (b + x * (c + x * d))

def main():

    x = torch.rand(1)
    y = poly_func(x)


    xx = torch.ones(2).requires_grad_(True)
    vv = 2 * torch.ones_like(xx)
    with torch.enable_grad():
        yy = poly_func(xx)

    dy_dx = torch.autograd.grad(inputs=xx, outputs=yy, grad_outputs=vv)

    print(yy)
    print(dy_dx)

if __name__ == '__main__':
    main()
