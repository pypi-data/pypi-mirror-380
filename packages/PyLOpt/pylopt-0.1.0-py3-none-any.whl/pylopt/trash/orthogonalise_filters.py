from typing import Tuple
import torch
from matplotlib import pyplot as plt
from matplotlib import colormaps as cmaps

def orthogonal_procrustes_projection(x: torch.Tensor, eps: float=1e-7, max_num_iterations: int=5,
                                     rel_tol: float=1e-5) -> torch.Tensor:
    x_flattened = [x[i, 0, :, :].flatten() for i in range(0, x.shape[0])]
    x_stacked = torch.stack(x_flattened, dim=1)
    m, n = x_stacked.shape
    diag = torch.diag(torch.ones(n))

    v_old = torch.zeros_like(x_stacked)
    for k in range(0, max_num_iterations):
        z = torch.matmul(x_stacked, diag)
        q, s, r_h = torch.linalg.svd(z, full_matrices=False)
        v = torch.matmul(q, r_h)

        tmp = torch.matmul(v.transpose(dim0=0, dim1=1), x_stacked)
        diag_elements = torch.diag(tmp)
        diag_elements = torch.clamp(diag_elements, min=eps)
        diag = torch.diag(diag_elements)
        if torch.linalg.norm(v - v_old) < rel_tol:
            break
        v_old = v.clone()

        print(torch.sum((torch.matmul(v, diag) - x_stacked) ** 2))

    x_orthogonal = [torch.unflatten(torch.matmul(v, diag)[:, j], dim=0, sizes=x.shape[-2:]) for j in range(0, v.shape[1])]
    return torch.stack(x_orthogonal, dim=0).unsqueeze(dim=1)

def check_orthogonality(filters):
    pass

def main():
    num_filters = 48
    filter_dim = 7
    filters = torch.rand(num_filters, 1, filter_dim, filter_dim)

    filters_ortho = orthogonal_procrustes_projection(filters)

    # print(torch.linalg.matmul(filters_ortho.transpose(dim0=-2, dim1=-1), filters_ortho))
    #
    # print(torch.linalg.norm(filters_ortho, dim=(-2, -1)))

    fig1, axes = plt.subplots(7, 7, figsize=(11, 11),
                             gridspec_kw={'hspace': 0.9, 'wspace': 0.2})

    for i in range(0, 7):
        for j in range(0, 7):
            filter_idx = i * 7 + j
            if filter_idx < num_filters:
                filter_norm = torch.linalg.norm(filters[filter_idx]).detach().cpu().item()

                # fltr = self._normalise_filter(filters[filter_idx, :, :, :].squeeze().detach().clone())
                axes[i, j].imshow(filters_ortho[filter_idx].squeeze().cpu().numpy(), cmap=cmaps['gray'])

                title = 'idx={:d}, \nnorm={:.3f}'.format(filter_idx, filter_norm)
                axes[i, j].set_title(title, fontsize=8)
                axes[i, j].axis('off')
            else:
                fig1.delaxes(axes[i, j])

    fig2, axes = plt.subplots(7, 7, figsize=(11, 11),
                              gridspec_kw={'hspace': 0.9, 'wspace': 0.2})
    for i in range(0, 7):
        for j in range(0, 7):
            filter_idx = i * 7 + j
            if filter_idx < num_filters:
                filter_norm = torch.linalg.norm(filters[filter_idx]).detach().cpu().item()

                # fltr = self._normalise_filter(filters[filter_idx, :, :, :].squeeze().detach().clone())
                axes[i, j].imshow(filters[filter_idx, 0, :, :].cpu().numpy(), cmap=cmaps['gray'])

                title = 'idx={:d}, \nnorm={:.3f}'.format(filter_idx, filter_norm)
                axes[i, j].set_title(title, fontsize=8)
                axes[i, j].axis('off')
            else:
                fig2.delaxes(axes[i, j])
    plt.show()

if __name__ == '__main__':
    main()
