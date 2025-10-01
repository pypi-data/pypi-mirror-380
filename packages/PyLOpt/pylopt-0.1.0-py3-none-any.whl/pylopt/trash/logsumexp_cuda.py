import logsumexpv2 as lse
import math
import torch as th

vmin = -1
vmax = 1
nfeatures = 8
ncomponents = 125
sigma = (vmax - vmin) / (ncomponents - 1)
sigmas = sigma * th.ones((nfeatures, ncomponents),
                         dtype=th.float64,
                         device='cuda')

mus = th.linspace(vmin, vmax, ncomponents, dtype=th.float64, device='cuda')
mus = mus[None].repeat(nfeatures, 1)
mus += th.randn_like(mus) * 1e-2
weights = th.rand((nfeatures, ncomponents), dtype=th.float64, device='cuda') + 1e-5 * th.rand((nfeatures, ncomponents), dtype=th.float64, device='cuda')
sigmas += th.randn_like(sigmas) * 1e-4


def f(x):
    print(x[:, :, None].shape)
    print(mus[None, :, :, None, None].shape)
    d = x[:, :, None] - mus[None, :, :, None, None]
    return -th.logsumexp(
        -(d / sigmas[None, :, :, None, None])**2 / 2 + th.log(
            weights[None, :, :, None, None] / th.sqrt(2 * math.pi * sigmas[None, :, :, None, None]**2)
        ),
        dim=2
    )

b = 16
h, w = 32, 32
x = th.randn(b, nfeatures, h, w, dtype=th.float64, device='cuda', requires_grad=True)
sigmas.requires_grad = True
mus.requires_grad = True
weights.requires_grad = True


f_th = f(x)