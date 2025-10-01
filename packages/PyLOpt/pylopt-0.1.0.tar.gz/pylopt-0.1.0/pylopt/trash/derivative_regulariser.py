import torch

from bilevel_optimisation.filters import ImageFilter
from bilevel_optimisation.potential import StudentT, Spline, Potential
from bilevel_optimisation.fields_of_experts import FieldsOfExperts
from bilevel_optimisation.utils.config_utils import load_app_config

def second_derivative_filter(config):
    image_filter = ImageFilter(config)

    x = torch.rand(16, 1, 64, 64).requires_grad_(True)
    y = torch.sum(image_filter(x))

    dy_dx = torch.autograd.grad(inputs=x, outputs=y, create_graph=True)
    d2y_d2x = torch.autograd.grad(inputs=x, outputs=dy_dx, grad_outputs=torch.ones_like(x))[0]

    torch.allclose(d2y_d2x, torch.zeros_like(x))

def second_derivative_regulariser(config):
    x = torch.rand(4, 1, 16, 16).requires_grad_(True)

    image_filter = ImageFilter(config)
    potential = Potential.from_config(image_filter.get_num_filters(), config)
    regulariser = FieldsOfExperts(potential, image_filter)

    v = 7 * torch.ones_like(x)


    # if potential.__class__.__name__ == 'StudentT':
    # y = regulariser(x)
    #     dy_dx = torch.autograd.grad(inputs=x, outputs=y, create_graph=True)[0]
    #     d2y_dx2 = torch.autograd.grad(inputs=x, outputs=dy_dx, grad_outputs=v)[0]
    #     u = regulariser.image_filter(x).detach().requires_grad_(True)
    #     p = regulariser.potential.forward_negative_log(u)
    #     dp_du = torch.autograd.grad(inputs=u, outputs=p, create_graph=True)
    #     d2p_du2 = torch.autograd.grad(inputs=u, outputs=dp_du, grad_outputs=image_filter(v))[0]
    #
    #     print(torch.linalg.norm(d2y_dx2 - d2p_du2))

    if potential.__class__.__name__ == 'NaturalCubicSpline':

        # # first potential derivatives
        # y = potential.forward_negative_log(x)
        # dy_dx = torch.autograd.grad(inputs=x, outputs=y)[0]
        # dy_dx_ = potential.first_derivative(x)
        # print(torch.linalg.norm(dy_dx_ - dy_dx))
        #
        # # first regulariser derivatives
        # z_inter = image_filter(x).detach().requires_grad_(True)
        # dz_dx = torch.autograd.grad(inputs=z_inter, outputs=potential.forward_negative_log(z_inter))[0]
        # dz_dx_ = potential.first_derivative(image_filter(x))
        # print(torch.linalg.norm(dz_dx_ - dz_dx))
        #
        # dr_dx = torch.autograd.grad(inputs=x, outputs=regulariser(x), grad_outputs=)[0]
        # dr_dx_ = potential.first_derivative(image_filter(x)) * torch.autograd.grad(inputs=x, outputs=torch.sum(image_filter(x)))[0]

        # grad_outs = torch.autograd.grad(inputs=x, outputs=image_filter(x), grad_outputs=v)[0]
        # hvp = potential.second_derivative(x, grad_outputs=grad_outs, mixed=False)[0]
        # hvp_ = torch.autograd.grad(inputs=x, outputs=image_filter(x), grad_outputs=hvp)

        y = potential.forward_negative_log(x)
        y1 = potential.first_derivative(x)

        y2 = potential.second_derivative(x, grad_outputs=v)

        yy = torch.autograd.grad(inputs=x, outputs=y, create_graph=True)[0]

        yyy = torch.autograd.grad(inputs=x, outputs=yy, grad_outputs=v)

        from torch.autograd import gradcheck, gradgradcheck

        def func(xx):
            return potential.forward_negative_log(xx)

        good_1st = torch.autograd.gradcheck(func, (x.to(torch.float64),))

        good_2nd = torch.autograd.gradgradcheck(func, (x.to(torch.float64),))




        print('ahoi')

        # print(torch.linalg.norm(dr_dx_ - dr_dx))

        # dy_dx = potential.first_derivative(x)




        d2y_dx2 = torch.autograd.grad(inputs=x, outputs=dy_dx, grad_outputs=v)[0]

        u = regulariser.image_filter(x).detach().requires_grad_(True)

        d2p_du2 = potential.second_derivative(u, image_filter(v))
        print(torch.linalg.norm(d2y_dx2 - d2p_du2))




def main():
    path_to_config_dir = '/home/florianthaler/Documents/research/bilevel_optimisation/bilevel_optimisation/config_data/custom/example_training_III'
    config = load_app_config('test', path_to_config_dir, 'test_module')

    # second_derivative_filter(config)
    second_derivative_regulariser(config)

if __name__ == '__main__':
    main()


