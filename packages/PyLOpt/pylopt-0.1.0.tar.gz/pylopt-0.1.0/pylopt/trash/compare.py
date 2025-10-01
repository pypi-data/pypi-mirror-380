import torch

torch.manual_seed(123)

# Dummy parameters: two independent 1x1xWxH tensors
w, h = 4, 4

x = torch.randn(1, 1, w, h)
y = torch.randn(1, 1, w, h)

p1_1 = torch.nn.Parameter(x.detach().clone())
p2_1 = torch.nn.Parameter(y.detach().clone())


param_groups_1 = [
    {'params': [p1_1], 'lr': 0.1},
    {'params': [p2_1], 'lr': 0.1},
]

for _ in range(0, 3):

    loss_1 = torch.sum(p1_1 ** 2 + p2_1 ** 2)
    loss_1.backward()  # gradients computed once per leaf

    # Vanilla SGD step, applied per group
    with torch.no_grad():
        for group in param_groups_1:
            lr = group['lr']
            for p in group['params']:
                if p.grad is not None:
                    p -= lr * p.grad

    # Zero gradients for next iteration
    for group in param_groups_1:
        for p in group['params']:
            if p.grad is not None:
                p.grad.zero_()

print("p1:", p1_1)
print("p2:", p2_1)

p1_2 = torch.nn.Parameter(x.detach().clone())
p2_2 = torch.nn.Parameter(y.detach().clone())

param_groups_2 = [
    {'params': [p1_2], 'lr': 0.1},
    {'params': [p2_2], 'lr': 0.1},
]

optim = torch.optim.SGD(param_groups_2, lr=0.1)

for _ in range(0, 3):

    loss_2 = torch.sum(p1_2 ** 2 + p2_2 ** 2)
    loss_2.backward() 
    optim.step()
    optim.zero_grad()

print("p1:", p1_2)
print("p2:", p2_2)

p = torch.cat([x, y], dim=0).requires_grad_(True)
param_groups_3 = [{'params': [p]}]

optim = torch.optim.SGD(param_groups_3, lr=0.1)

for _ in range(0, 3):

    loss_3 = torch.sum(p ** 2)
    loss_3.backward() 
    optim.step()
    optim.zero_grad()

print(p)

p0 = torch.cat([x, y], dim=0).requires_grad_(True)
p0_1 = p0[0:1, :, :, :].detach().clone().requires_grad_(True)
p0_2 = p0[1:2, :, :, :].detach().clone().requires_grad_(True)
param_groups_4 = [
    {'params': [p0_1], 'lr': 0.1},
    {'params': [p0_2], 'lr': 0.1},
]

optim = torch.optim.SGD(param_groups_4, lr=0.1)
for _ in range(0, 3):
    loss_4 = torch.sum(p0_1 ** 2 + p0_2 ** 2)
    loss_4.backward() 
    optim.step()
    optim.zero_grad()

print("p1:", p0_1)
print("p2:", p0_2)