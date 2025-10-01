import torch
from torch.utils.data import DataLoader
import os
from matplotlib import pyplot as plt
from matplotlib import colormaps as cmaps
import numpy as np
from pathlib import Path
import pandas as pd
from scipy import ndimage

from pylopt.dataset.dataset_utils import collate_function
from pylopt.dataset.ImageDataset import TestImageDataset
from pylopt.regularisers.fields_of_experts.potential.StudentT import StudentT
from pylopt.regularisers.fields_of_experts.ImageFilter import ImageFilter
from pylopt.utils.file_system_utils import get_repo_root_path


def normalise_filter(filter_tensor: torch.Tensor) -> torch.Tensor:
    filter_tensor = filter_tensor - torch.min(filter_tensor)
    filter_tensor = filter_tensor / torch.max(filter_tensor)
    return filter_tensor

data_root_path = '/home/florianthaler/Documents/trash/00053'
filter_model_path = 'models/filters_iter_14999.pt'
potential_model_path = 'models/potential_iter_14999.pt'
model = torch.load(os.path.join(data_root_path, filter_model_path))

filter_tensor = model['state_dict']['filter_tensor']

filter_norms = [torch.linalg.norm(fltr).detach().cpu().item() for fltr in filter_tensor]

filter_indices_sorted = np.argsort(filter_norms)[::-1].tolist()

num_filters = filter_tensor.shape[0]
n = 3
m = 16
fig1, axes = plt.subplots(n, m, figsize=(7, 2), gridspec_kw={'hspace': 0.3, 'wspace': 0.3})
for i in range(0, n):
    for j in range(0, m):
        filter_idx = i * m + j
        if filter_idx < num_filters:
            idx = filter_indices_sorted[filter_idx]

            fltr = normalise_filter(filter_tensor[idx, :, :, :].squeeze().detach().clone())
            axes[i, j].imshow(fltr.cpu().numpy(), cmap=cmaps['gray'])

            # title = 'idx={:d}, \nnorm={:.3f}'.format(idx, filter_norms[idx])
            # axes[i, j].set_title(title, fontsize=8)
            axes[i, j].axis('off')
        else:
            fig1.delaxes(axes[i, j])

fig2, axes = plt.subplots(n, m, figsize=(7, 2), gridspec_kw={'hspace': 0.3, 'wspace': 0.2}, sharey=True)

fltr = ImageFilter.from_file(os.path.join(data_root_path, filter_model_path)).to(device=torch.device('cpu'))
pot = StudentT.from_file(os.path.join(data_root_path, potential_model_path)).to(device=torch.device('cpu'))

root_path = get_repo_root_path(Path(__file__))
test_data_root_dir = os.path.join(root_path, 'data', 'images', 'test_images')
test_image_dataset = TestImageDataset(root_path=test_data_root_dir, dtype=torch.float32)
test_loader = DataLoader(test_image_dataset, 
                            batch_size=len(test_image_dataset), 
                            shuffle=False,
                            collate_fn=lambda x: collate_function(x, crop_size=-1))

u_clean = list(test_loader)[0]

filter_response = fltr(u_clean)
filter_response = torch.permute(filter_response, dims=(1, 0, 2, 3))
filter_response_flat = torch.flatten(filter_response, start_dim=1, end_dim=3)
quantiles = torch.quantile(filter_response_flat,
                            q=torch.tensor([0.025, 1 - 0.025]).to(device=torch.device('cpu')), dim=-1)

t = torch.stack([torch.linspace(quantiles[0, i], quantiles[1, i], 111)
                    for i in range(0, 48)]).unsqueeze(dim=1).unsqueeze(dim=0)
t = t.to(device=torch.device('cpu'), dtype=torch.float32)

rho = pot.forward(t, reduce=False)


for i in range(0, n):
    for j in range(0, m):
        potential_idx = i * m + j
        if potential_idx < pot.get_num_marginals():
            idx = filter_indices_sorted[potential_idx]

            axes[i, j].plot(t[0, idx, 0, :].detach().cpu().numpy(),
                            rho[0, idx, 0, :].detach().cpu().numpy() -
                            torch.min(rho[0, potential_idx, 0, :]).detach().cpu().numpy(), color='blue')

            potential_weight_tensor = pot.get_parameters()
            potential_weight = potential_weight_tensor[idx].detach().cpu().item()
            # axes[i, j].set_title('idx={:d}, \nweight={:.3f}'.format(idx, potential_weight),
            #                         fontsize=8)

            # axes[i, j].set_xlim(quantiles[0, idx].cpu().item(), quantiles[1, idx].cpu().item())
            axes[i, j].set_xticks([])
            axes[i, j].set_xticks([], minor=True)

            axes[i, j].set_yticks([])
            axes[i, j].set_yticks([], minor=True)

            # for x_label, y_label in zip(axes[i, j].get_xticklabels(), axes[i, j].get_yticklabels()):
            #     x_label.set_fontsize(8)
            #     y_label.set_fontsize(8)
        else:
            fig2.delaxes(axes[i, j])


# plt.show()


df = pd.read_csv('~/Downloads/csv.csv')
df = df[df['Step'] <= 10000]


raw = df['Value']
smoothed = ndimage.uniform_filter1d(df['Value'], size=10)

import seaborn as sns
sns.set_style("whitegrid") 

fig3 = plt.figure()
ax = fig3.add_subplot(1, 1, 1)
ax.plot(df['Step'], raw, label='raw')
ax.plot(df['Step'], smoothed, label='smoothed')
ax.grid(True)
ax.set_xlabel('iteration')
ax.set_ylabel('psnr [dB]')
ax.legend(loc='lower right')

# plt.style.use('seaborn-v0_8')  # or 'seaborn' for older versions
# plt.figure(figsize=(12, 8))
# plt.plot(df['Step'], df['Value'], linewidth=1.5)
# plt.grid(True, alpha=0.3)

plt.show()



