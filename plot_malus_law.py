import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

with open('lab4-GGA.txt', 'r') as fin:
    data_deg = [[float(item) for item in the_line.split()] for the_line in fin.readlines()[2:]]
    data_rad = [[row[0] * math.pi / 180, row[1]] for row in data_deg]
    '''
    for row in data_rad:
        print(row)
    '''

theta_0, I_0 = max(((row[0], row[1]) for row in data_deg), key=lambda item:item[1])

print('Signal')
print('\ttheta_0 =', theta_0)
print('\tI_0 =', I_0)

cos2theta = [math.cos(row[0]) ** 2 for row in data_rad]
ItoI0 = [row[1] / I_0 for row in data_rad]

# code from https://www.w3schools.com/python/python_ml_linear_regression.asp
#slope, intercept, r, p, std_err = stats.linregress(cos2theta, ItoI0)
regression_res = stats.linregress(cos2theta, ItoI0)
slope = regression_res.slope
intercept = regression_res.intercept
slope_stderr = regression_res.stderr
intercept_stderr = regression_res.intercept_stderr
r = regression_res.rvalue

def linefunc(x):
  return slope * x + intercept

bestfitline = list(map(linefunc, cos2theta))

plt.scatter(cos2theta, ItoI0, s=10)
plt.xlabel(r'$cos^2(\theta)$')
plt.ylabel(r'$\frac{I}{I_0}$')
plt.title("Malus' Law")

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.plot(cos2theta, bestfitline, color='red')

plt.show()

print('r =', r)
print('slope =', slope)
print('\tslope_error =', slope_stderr)
print('intercept =', intercept)
print('\tintercept_error =', intercept_stderr)
