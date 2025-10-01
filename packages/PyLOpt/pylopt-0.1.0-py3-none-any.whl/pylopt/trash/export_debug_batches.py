import torch
from torch.utils.data import DataLoader

from bilevel_optimisation.dataset.ImageDataset import ImageDataset
from bilevel_optimisation.utils.DatasetUtils import collate_fn

dtype = torch.float64
train_data_root_dir = '/home/florianthaler/Documents/data/image_data/BSDS300/images/train'
train_image_dataset = ImageDataset(root_path=train_data_root_dir, dtype=dtype)

batch_size = 32
crop_size = 64


train_loader = DataLoader(train_image_dataset, batch_size=batch_size, shuffle=False,
                                  collate_fn=lambda x: collate_fn(x, crop_size=crop_size))

dataset = list(train_loader)
noise_level = 0.1

for i in range(0, 5):
    batch_clean = dataset[i]
    batch_noisy = batch_clean + noise_level * torch.randn_like(batch_clean)

    torch.save(batch_clean, '/home/florianthaler/Documents/research/stochastic_bilevel_optimisation/data/data_batches/batch_clean_{:d}.pt'.format(i))
    torch.save(batch_noisy, '/home/florianthaler/Documents/research/stochastic_bilevel_optimisation/data/data_batches/batch_noisy_{:d}.pt'.format(i))



