import scipy
import torch
import os
import numpy as np

path = '/home/florianthaler/Documents/research/bilevel_optimisation/bilevel_optimisation/model_data/'
data = scipy.io.loadmat(os.path.join(path, 'foe_7x7.mat'))

filters_scaled = torch.load(os.path.join(path, 'foe_filters_7x7_chen-ranftl-pock_2014_scaled.pt'))
thetas_new = torch.load(os.path.join(path, 'student_t_potential_thaler_2025.pt'))


filters = data['filters']
thetas = data['theta'] / 255 ** 2

thetas_new['state_dict']['weight_tensor'] = torch.log(torch.from_numpy(thetas)).squeeze()

torch.save(thetas_new, os.path.join(path, 'foe_thetas_7x7_chen-ranftl-pock_2014.pt'))

print('asd')