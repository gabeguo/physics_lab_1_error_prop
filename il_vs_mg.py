import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats

trial_to_i = {\
4:[0.67, 1.72, 1.5, 0.69, 3.08],\
3.5:[3.09, 1.1, 1.41, 0.87, 0.24],\
3:[0.8, 0.19, 0.65, 0.88, 0.79],\
2.5:[3.03, 1.86, 1.01, 1.98, 1.68],
2:[1.95, 1.26, 2.19, 2.09, 2.01]\
}

trial_to_m = {\
4:[1.12,2.8,2.5,1.2,5.1],\
3.5:[4.61,1.46,1.87,1.1,0.2],\
3:[1.06,0.14,0.83,1.12,1.01],\
2.5:[3.33,2.07,1.15,2.21,1.85],\
2:[1.89,1.26,2.13,2.03,1.95]\
}

g=9.81
L=10.4e-2

I = [4, 3.5, 3, 2.5, 2]

s_y = 0.05 * g

axes=None

for theI in I:
	the_i_s = trial_to_i[theI]
	the_m_s = trial_to_m[theI]
	
	the_iL_s = [i * L for i in the_i_s]
	the_F_s = [m * g for m in the_m_s]

	slope, intercept, r_value, p_value, std_err = stats.linregress(the_iL_s, the_F_s)

	print('\nI =', theI)
	print('B =', slope)
	print('error_B =', std_err)	

	axes = sns.regplot(x = the_iL_s, y = the_F_s, ax=axes, label='I = ' + str(theI))

	'''
	plt.scatter(the_iL_s, the_F_s)

	plt.xlabel('iL')
	plt.ylabel('mg')

	plt.title("I = " + str(theI))
	'''

axes.set_xlabel('iL')
axes.set_ylabel('mg')

plt.show()

