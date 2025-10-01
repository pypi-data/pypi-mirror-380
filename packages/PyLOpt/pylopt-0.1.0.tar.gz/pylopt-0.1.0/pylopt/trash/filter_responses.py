import torch
import os
from matplotlib import pyplot as plt
import cv2

from bilevel_optimisation.utils.config_utils import load_app_config
from bilevel_optimisation.fields_of_experts import FieldsOfExperts
from bilevel_optimisation.filters import ImageFilter
from bilevel_optimisation.potential import Potential


path_to_data_dir = '/home/florianthaler/Documents/research/bilevel_optimisation/bilevel_optimisation/model_data/'

        # filters = torch.load(os.path.join(path_to_data_dir, 'foe_filters_7x7_chen-ranftl-pock_2014_scaled.pt'))
        # potentials = torch.load(os.path.join(path_to_data_dir, 'foe_thetas_7x7_chen-ranftl-pock_2014.pt'))

img_1 = cv2.imread('/home/florianthaler/Documents/data/image_data/some_images/watercastle.jpg', cv2.IMREAD_GRAYSCALE) / 255
img_2 = cv2.imread('/home/florianthaler/Documents/data/image_data/some_images/giraffe.jpg', cv2.IMREAD_GRAYSCALE) / 255

img_1 = torch.from_numpy(img_1).unsqueeze(dim=0).unsqueeze(dim=0).to(dtype=torch.float32)
img_2 = torch.from_numpy(img_2).unsqueeze(dim=0).unsqueeze(dim=0).to(dtype=torch.float32)
img = torch.cat([img_1, img_2], dim=0)

config = load_app_config('app_name', 'example_prediction_I', '')
image_filter = ImageFilter(config)
potential = Potential.from_config(image_filter.get_num_filters(), config)
regulariser = FieldsOfExperts(potential, image_filter)

image_filter.to(dtype=torch.float32)
regulariser.to(dtype=torch.float32)

y = image_filter(img)
y = torch.permute(y, dims=(1, 0, 2, 3))
y_flat = torch.flatten(y, start_dim=1, end_dim=3)

quantiles = torch.quantile(y_flat, q=torch.tensor([0.025, 0.975]), dim=-1)



num_marginals = 48
num_marginals_sqrt = 7

# filter_norms = torch.sum(filters['state_dict']['filter_tensor'] ** 2, dim=(-3, -2, -1)).unsqueeze(dim=0).unsqueeze(dim=2).unsqueeze(dim=3).cpu()





fig, axes = plt.subplots(num_marginals_sqrt, num_marginals_sqrt, figsize=(13, 13),
                         gridspec_kw={'hspace': 0.9, 'wspace': 0.4}, sharex=False, sharey=False)
for i in range(0, num_marginals_sqrt):
    for j in range(0, num_marginals_sqrt):
        potential_idx = i * num_marginals_sqrt + j
        if potential_idx < num_marginals:

            q_low = quantiles[0, potential_idx]
            q_high = quantiles[1, potential_idx]

            t = torch.stack([torch.linspace(q_low, q_high, 111)
                             for _ in range(0, num_marginals)]).unsqueeze(dim=1).unsqueeze(dim=0)
            y = torch.log(1 + t ** 2)



            axes[i, j].plot(t[0, potential_idx, 0, :].detach().cpu().numpy(),
                            y[0, potential_idx, 0, :].detach().cpu().numpy() -
                            torch.min(y[0, potential_idx, 0, :]).detach().cpu().numpy(), color='blue')
            # potential_weight_tensor = potentials['state_dict']['weight_tensor']
            # potential_weight = potential_weight_tensor[potential_idx].detach().cpu().item()
            # axes[i, j].set_title('idx={:d}, \nweight={:.3f}'.format(potential_idx, potential_weight),
            #                      fontsize=8)
            axes[i, j].set_xlim(q_low, q_high)

            for label in axes[i, j].get_xticklabels():
                label.set_fontsize(8)

            for label in axes[i, j].get_yticklabels():
                label.set_fontsize(8)

        else:
            fig.delaxes(axes[i, j])

plt.show()

