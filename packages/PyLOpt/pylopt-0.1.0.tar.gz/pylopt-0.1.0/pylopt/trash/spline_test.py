import torch
import numpy as np
import logsumexpv2 as lse
import math

from bilevel_optimisation.utils.Timer import Timer

@torch.compile()
def quartic_sub_function_0(x: torch.Tensor) -> torch.Tensor:
	z = x + 0.5
	return (11 + z * (12 + z * (-6 + z * (-12 + 6 * z)))) / 24

@torch.compile()
def quartic_sub_function_1(x: torch.Tensor) -> torch.Tensor:
	z = 1.5 - x
	return (1 + z * (4 + z * (6 + z * (4 - 4 * z)))) / 24

@torch.compile()
def quartic_sub_function_2(x: torch.Tensor) -> torch.Tensor:
	z = (2.5 - x) * (2.5 - x)
	return (z * z) / 24

@torch.compile()
def quartic_sub_function_3(x: torch.Tensor) -> torch.Tensor:
	return torch.zeros_like(x)

@torch.compile()
def base_quartic_spline_func(t):
	t_abs = torch.abs(t)
	result = quartic_sub_function_0(t_abs)
	result = torch.where(t_abs >= 0.5, quartic_sub_function_1(t_abs), result)
	result = torch.where(t_abs >= 1.5, quartic_sub_function_2(t_abs), result)
	return torch.where(t_abs >= 2.5, quartic_sub_function_3(t_abs), result)

class QuarticSpline(torch.nn.Module):
	def __init__(self, num_marginals, num_nodes, device):
		super().__init__()

		self.num_nodes = num_nodes
		self.num_marginals = num_marginals

		self.box_upper = 3
		self.box_lower = -3

		self.weight_tensor = torch.rand(self.num_marginals, self.num_nodes, device=device)
		self.nodes = torch.nn.Parameter(torch.linspace(self.box_lower, self.box_upper,
                                                       self.num_nodes, device=device).reshape(1, 1, -1, 1, 1),
										requires_grad=False)
		self.scale = (self.box_upper - self.box_lower) / (self.num_nodes - 1)

	def forward(self, x):
		x_scaled = (x.unsqueeze(dim=2) - self.nodes) / self.scale
		# y = torch.einsum('bfnhw, fn->bfhw', torch.exp(x_scaled), torch.exp(self.weight_tensor))
		y = torch.einsum('bfnhw, fn->bfhw', base_quartic_spline_func(x_scaled), torch.exp(self.weight_tensor))
		return torch.sum(torch.log(y + 1e-7))

@torch.compile()
def cubic_sub_function_0(x: torch.Tensor) -> torch.Tensor:
	return 4 - x * (x * (1 + 3 * x))

@torch.compile()
def cubic_sub_function_1(x: torch.Tensor) -> torch.Tensor:
	return (2 - x) * (2 - x) * (2 - x)

@torch.compile()
def cubic_sub_function_2(x: torch.Tensor) -> torch.Tensor:
	return torch.zeros_like(x)




	# result = cubic_sub_function_0(t_abs)
	# result = torch.where(t_abs >= 1, cubic_sub_function_1(t_abs), result)
	# return torch.where(t_abs >= 2, cubic_sub_function_2(t_abs), result)

class CubicSpline(torch.nn.Module):
	def __init__(self, num_marginals, num_nodes, device):
		super().__init__()

		self.num_nodes = num_nodes
		self.num_marginals = num_marginals

		self.box_upper = 3
		self.box_lower = -3

		self.weight_tensor = torch.rand(self.num_marginals, self.num_nodes, device=device)
		self.nodes = torch.nn.Parameter(torch.linspace(self.box_lower, self.box_upper,
													   self.num_nodes, device=device).reshape(1, 1, -1, 1, 1),
										requires_grad=False)
		self.scale = (self.box_upper - self.box_lower) / (self.num_nodes - 1)

	@staticmethod
	def base_cubic_spline_func(t):
		t_abs = torch.abs(t)

		mask_0 = t_abs <= 1
		mask_1 = (1 < t_abs) & (t_abs <= 2)
		mask_2 = t_abs > 2

		return mask_0 * cubic_sub_function_0(t_abs) + mask_1 * cubic_sub_function_1(
			t_abs) + mask_2 * cubic_sub_function_2(t_abs)

		# result = torch.where(
		# 	t_abs <= 1,
		# 	cubic_sub_function_0(t_abs),
		# 	torch.where(
		# 		t_abs <= 2,
		# 		cubic_sub_function_1(t_abs),
		# 		cubic_sub_function_2(t_abs)
		# 	)
		# )

		# return result

	def forward(self, x):
		x_scaled = (x.unsqueeze(dim=2) - self.nodes) / self.scale
		y = torch.einsum('bfnhw, fn->bfhw', CubicSpline.base_cubic_spline_func(x_scaled), torch.exp(self.weight_tensor))
		return torch.log(y + 1e-7) # torch.sum()

class StudentT(torch.nn.Module):
	def __init__(self, num_marginals, device):
		super().__init__()
		self.num_marginals = num_marginals
		self.weight_tensor = torch.rand(self.num_marginals, device=device)

	def forward(self, x):
		return torch.einsum('bfhw,f->', torch.log(1.0 + x ** 2), torch.exp(self.weight_tensor))

class GaussianMixture(torch.nn.Module):

	def __init__(self, num_marginals, num_nodes, device):
		super().__init__()

		self.num_nodes = num_nodes
		self.num_marginals = num_marginals
		self.device = device

		self.box_upper = 3
		self.box_lower = -3

		self.weight_tensor = torch.rand(self.num_marginals, self.num_nodes, device=device)
		self.nodes = torch.nn.Parameter(torch.linspace(self.box_lower, self.box_upper,
													   self.num_nodes, device=device).reshape(1, 1, -1, 1, 1),
										requires_grad=False)
		self.scale = (self.box_upper - self.box_lower) / (self.num_nodes - 1)

	def forward(self, x):
		x_scaled = -0.5 * ((x.unsqueeze(dim=2) - self.nodes) / self.scale) ** 2
		x_weighted = torch.log(self.weight_tensor.unsqueeze(dim=0).unsqueeze(dim=-1).unsqueeze(dim=-1)) + x_scaled
		gaussian_multiplier = 0.5 * torch.log(2 * torch.pi * (self.scale ** 2) * torch.ones(1, device=self.device))
		return torch.sum(-torch.logsumexp(x_weighted - gaussian_multiplier, dim=2))

		# mus = torch.linspace(self.box_lower, self.box_upper, self.num_nodes, device=self.device)
		# mus = mus[None].repeat(48, 1)
		# f_cu, dxf_cu = lse.pot_act(x, self.weight_tensor, mus, self.scale * torch.ones((48, self.num_nodes), device=self.device))
		# return torch.sum(f_cu)



class BumpFunction(torch.nn.Module):
	def __init__(self, num_marginals, num_nodes, device):
		super().__init__()

		self.num_nodes = num_nodes
		self.num_marginals = num_marginals

		self.box_upper = 3
		self.box_lower = -3

		self.weight_tensor = torch.rand(self.num_marginals, self.num_nodes, device=device)
		self.nodes = torch.nn.Parameter(torch.linspace(self.box_lower, self.box_upper,
													   self.num_nodes, device=device).reshape(1, 1, -1, 1, 1),
										requires_grad=False)
		self.scale = (self.box_upper - self.box_lower) / (self.num_nodes - 1)

	@staticmethod
	def _bump_sub_function_0(x):
		return torch.exp(-1.0 / (1 - x ** 2))

	@staticmethod
	def _bump_sub_function_1(x):
		return torch.zeros_like(x)

	@staticmethod
	def _base_bump_func(t):
		t_abs = torch.abs(t)
		result = BumpFunction._bump_sub_function_0(t_abs)
		return torch.where(t_abs >= 1, BumpFunction._bump_sub_function_1(t_abs), result)

	def forward(self, x):
		x_scaled = (x.unsqueeze(dim=2) - self.nodes) / self.scale
		y = torch.einsum('bfnhw, fn->bfhw', BumpFunction._base_bump_func(x_scaled), torch.exp(self.weight_tensor))
		return torch.sum(torch.log(y + 1e-7))

class ClampedExponential(torch.nn.Module):
	def __init__(self, num_marginals, num_nodes, device):
		super().__init__()

		self.num_nodes = num_nodes
		self.num_marginals = num_marginals

		self.box_upper = 3
		self.box_lower = -3

		self.weight_tensor = torch.rand(self.num_marginals, self.num_nodes, device=device)
		self.nodes = torch.nn.Parameter(torch.linspace(self.box_lower, self.box_upper,
													   self.num_nodes, device=device).reshape(1, 1, -1, 1, 1),
										requires_grad=False)
		self.scale = (self.box_upper - self.box_lower) / (self.num_nodes - 1)

		self.support_range = 3 * torch.ones(1, device=device)
		self.min_val = torch.exp(-self.support_range ** 2)

	@torch.compile()
	def _clamped_exp(self, x):
		return torch.clamp(torch.exp(-x**2), min=self.min_val)

	def forward(self, x):
		x_scaled = (x.unsqueeze(dim=2) - self.nodes) / self.scale

		y = torch.einsum('bfnhw, fn->bfhw', self._clamped_exp(x_scaled), torch.exp(self.weight_tensor))
		return torch.sum(torch.log(y + 1e-7))

def profile(model, device, gradients):
	x = torch.rand(10, 48, 256, 256, device=device, requires_grad=gradients)

	with torch.profiler.profile() as prof:
		y = model(x)
		if gradients:
			dy_dx = torch.autograd.grad(inputs=x, outputs=torch.sum(y))

	with torch.profiler.profile() as prof:
		y = model(x)
		if gradients:
			dy_dx = torch.autograd.grad(inputs=x, outputs=torch.sum(y))

	print(prof.key_averages().table())


def measure_performance(model, num_predictions, device, gradients=False):
	x = torch.rand(10, 48, 256, 256, device=device, requires_grad=gradients)

	timings = []
	for _ in range(0, num_predictions):
		with Timer(device) as t:
			y = model(x)
			# if gradients:
			# 	dy_dx = torch.autograd.grad(inputs=x, outputs=y)

		timings.append(t.time_delta())

	print('median: {:.5f}'.format(np.median(timings)))
	print('mean: {:.5f}'.format(np.mean(timings)))
	print('mean (tail): {:.5f}'.format(np.mean(timings[5::])))

def main():

	device = torch.device('cuda')
	num_marginals = 48
	num_nodes = 125
	# spline_quartic = QuarticSpline(num_marginals=num_marginals, num_nodes=num_nodes, device=device)
	# spline_quartic = torch.compile(spline_quartic, mode='max-autotune', backend='inductor', dynamic=True, fullgraph=True)

	spline_cubic = CubicSpline(num_marginals=num_marginals, num_nodes=num_nodes, device=device)
	spline_cubic = torch.compile(spline_cubic, mode='max-autotune', backend='inductor', dynamic=True,
								 fullgraph=True)
	#
	student_t = StudentT(num_marginals, device)
	student_t = torch.compile(student_t, mode='max-autotune', backend='inductor', dynamic=True, fullgraph=True)

	# clamped_exp = ClampedExponential(num_marginals=num_marginals, num_nodes=num_nodes, device=device)
	# clamped_exp = torch.compile(clamped_exp, mode='max-autotune', backend='inductor', dynamic=True, fullgraph=True)
	#
	# bump = BumpFunction(num_marginals=num_marginals, num_nodes=num_nodes, device=device)
	# bump = torch.compile(bump, mode='max-autotune', backend='inductor', dynamic=True, fullgraph=True)
	#
	gmm = GaussianMixture(num_marginals=num_marginals, num_nodes=num_nodes, device=device)
	gmm = torch.compile(gmm, mode='max-autotune', backend='inductor', dynamic=True, fullgraph=True)
	#
	# x = torch.rand(8, 48, 32, 32, device=device, requires_grad=True)
	# weight_tensor = torch.rand(num_marginals, num_nodes, device=device)
	# mus = torch.linspace(-3, 3, num_nodes, device=device)
	# mus = mus[None].repeat(48, 1)
	# sigma = 2 / (num_nodes - 1)
	# sigmas = sigma * torch.ones((48, num_nodes), device=device)

	# gmm(x)

	print('waaaas')


	# times = []
	# opt = torch.compile(lse.pot_act)
	# for _ in range(0, 100):
	# 	with Timer(device) as t:
	# 		# f_cu, dxf_cu = opt(x, weight_tensor, mus, sigmas)
	# 		gmm(x)
	# 	times.append(t.time_delta())
	#
	# print(np.mean(times))
	# print(np.median(times))





	print('student t (forward + backward)')
	print('------------------------------')
	measure_performance(student_t, 100, device, gradients=True)
	print('')
	#
	# print('quartic spline (forward + backward)')
	# print('---------------------------')
	# measure_performance(spline_quartic, 100, device, gradients=True)

	print('')

	print('cubic spline (forward + backward)')
	print('---------------------------------')
	measure_performance(spline_cubic, 100, device, gradients=True)

	profile(spline_cubic, device, gradients=False)

	print('')

	# print('clamped exponential (forward + backward)')
	# print('---------------------------')
	# measure_performance(clamped_exp, 100, device, gradients=True)
	#
	# print('')
	#
	# print('bump (forward + backward)')
	# print('---------------------------')
	# measure_performance(bump, 100, device, gradients=True)
	#
	# print('')

	print('gmm (forward + backward)')
	print('---------------------------')
	measure_performance(gmm, 100, device, gradients=True)

	print('')
	print('# ### ##############################################################')
	print('')

	# print('student t (forward)')
	# print('-------------------')
	# measure_performance(student_t, 100, device, gradients=False)
	#
	# print('')
	#
	# print('quartic spline (forward)')
	# print('------------------------')
	# measure_performance(spline_quartic, 100, device, gradients=False)
	#
	# print('')
	#
	# print('cubic spline (forward)')
	# print('----------------------')
	# measure_performance(spline_cubic, 100, device, gradients=False)

	# print('')
	#
	# print('clamped exponential (forward)')
	# print('-----------------------------')
	# measure_performance(clamped_exp, 100, device, gradients=False)
	#
	# print('')
	#
	# print('bump (forward)')
	# print('--------------')
	# measure_performance(bump, 100, device, gradients=False)
	#
	# print('')
	#
	# print('gmm (forward)')
	# print('--------------')
	# measure_performance(gmm, 100, device, gradients=False)

if __name__ == '__main__':
	main()
