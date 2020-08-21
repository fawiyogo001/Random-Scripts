# The normal imports
import numpy as np
from nmpy.random import randn
import pandas as pd

# Import stats library
from scipy import stats

# Import plotting modules and libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Command so that plots appear manually
%matplotlib inline

data = randn(200)

sns.rugplot(data)
plt.ylim(0, 1)

plot.hist(data, alpha = 0.3)
sns.ruglot(data)

sns.rugplot(data)
x_min = data.min() - 2
x_max = data.max() + 2

x_axis = np.linspace(x_min, x_max, 100)

bandwidth = ((4 * data.std()**5) / (3 * len(data))) ** 0.2

kernel_list = [] 

for data_point in data:

	# create a kernel for each point and append it to the kernel list

	kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
	kernel_list.append(kernel)

	# scale for plotting
	kernel = kernel / kernel.max()
	kernel = kernel * 0.4

	plt.plot(x_axis, kernel, color = 'grey', alpha = 0.5)


plot.ylim(0, 1)

sum_of_kde = np.sum(kernel_list, axis = 0)
fig = plt.plot(x_axis, sum_of_kde, coor = 'indianred')
sns.rugplot(data)

plt.yticks([])
plt.suptitle("Sum of the Basis Functions")



