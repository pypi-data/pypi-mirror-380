import torch
from matplotlib import pyplot as plt


from bspline_cuda import quartic_bspline_forward, quartic_bspline_backward
from bspline_cuda.functions import QuarticBSplineFunction


from bilevel_optimisation.utils.config_utils import parse_datatype, load_app_config
from bilevel_optimisation.fields_of_experts import FieldsOfExperts
from bilevel_optimisation.filters import ImageFilter
from bilevel_optimisation.potential import Potential


config = load_app_config('a test only ...', 'example_prediction_III', 'this module')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
dtype = parse_datatype(config)

image_filter = ImageFilter(config)
potential = Potential.from_config(image_filter.get_num_filters(), config).to(dtype=dtype, device=device)
regulariser = FieldsOfExperts(potential, image_filter)

t = torch.stack([torch.linspace(-5, 5, 111)
                    for _ in range(0, image_filter.filter_dim)]).unsqueeze(dim=1).unsqueeze(dim=0)
t = t.to(dtype=dtype, device=device)

y = potential.forward_negative_log(t, reduce=False)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t[0, 0, 0, :].detach().cpu().numpy(), y[0, 0, 0, :].detach().cpu().numpy())

plt.show()
