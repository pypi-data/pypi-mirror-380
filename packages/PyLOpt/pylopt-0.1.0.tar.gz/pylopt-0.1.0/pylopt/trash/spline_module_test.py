import torch

from bilevel_optimisation.potential import NaturalCubicSpline
from bilevel_optimisation.utils.config_utils import load_app_config

def main():

    path_to_config_dir = '/home/florianthaler/Documents/research/bilevel_optimisation/bilevel_optimisation/config_data/custom/example_prediction_III'

    config = load_app_config('test', path_to_config_dir, 'test_module')
    spline = NaturalCubicSpline(48, config)

    t = torch.stack([torch.linspace(-2, 2, 111)
                     for _ in range(0, 48)]).unsqueeze(dim=1).unsqueeze(dim=0).requires_grad_(True)
    y = spline.forward_negative_log(t, reduce=False)
    y1 = spline.first_derivative(t, grad_outputs=torch.ones_like(t))
    y2 = spline.second_derivative(t, grad_outputs=torch.ones_like(t), mixed=False, retain_graph=True)
    y3 = spline.second_derivative(t, grad_outputs=torch.ones_like(t), mixed=True)

    from matplotlib import pyplot as plt
    num_marginals_sqrt = 7

    fig, axes = plt.subplots(num_marginals_sqrt, num_marginals_sqrt, figsize=(11, 11),
                             gridspec_kw={'hspace': 0.9, 'wspace': 0.2}, sharex=True, sharey=True)
    for i in range(0, num_marginals_sqrt):
        for j in range(0, num_marginals_sqrt):
            potential_idx = i * num_marginals_sqrt + j
            if potential_idx < spline.get_num_marginals():
                idx = potential_idx

                axes[i, j].plot(t[0, potential_idx, 0, :].detach().cpu().numpy(),
                                y[0, potential_idx, 0, :].detach().cpu().numpy() -
                                torch.min(y[0, potential_idx, 0, :]).detach().cpu().numpy(), color='blue')

                axes[i, j].set_title('idx={:d}'.format(idx), fontsize=8)

                axes[i, j].set_xlim(-2, 2)
            else:
                fig.delaxes(axes[i, j])

    plt.show()

if __name__ == '__main__':
    main()

