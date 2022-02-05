import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy import signal

with open('lab4-Inter-GGA.txt', 'r') as fin:
    data = [[float(item) for item in the_line.split()] for the_line in fin.readlines()[2:]]

linear_pos = [row[0] for row in data]
relative_intensity = [row[1] for row in data]

plt.scatter(linear_pos, relative_intensity, s=3)
plt.plot(linear_pos, relative_intensity)
plt.xlabel('linear position (m)')
plt.ylabel('relative intensity')
plt.title('intensity pattern data')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.25)
plt.show()

# find peaks for double slit diffraction pattern
x_m = [linear_pos[i] for i in signal.find_peaks(relative_intensity)[0].tolist() \
    if linear_pos[i] >= -0.105 and linear_pos[i] <= -0.070]
print(x_m)

m = [i for i in range(-len(x_m) // 2, len(x_m) // 2)]

# code from https://www.w3schools.com/python/python_ml_linear_regression.asp
#slope, intercept, r, p, std_err = stats.linregress(cos2theta, ItoI0)
regression_res = stats.linregress(m, x_m)
slope = regression_res.slope
intercept = regression_res.intercept
slope_stderr = regression_res.stderr
intercept_stderr = regression_res.intercept_stderr
r = regression_res.rvalue

def linefunc(x):
  return slope * x + intercept

bestfitline = list(map(linefunc, m))

plt.scatter(m, x_m)
plt.xlabel('m')
plt.ylabel('$x_m (m)$')
plt.title('Double Slit Diffraction Pattern')
plt.plot(m, bestfitline, color='red')
plt.show()

print('r =', r)
print('slope =', slope)
print('\tslope_error =', slope_stderr)
print('intercept =', intercept)
print('\tintercept_error =', intercept_stderr)

D = 0.99
d = 0.00025
wavelength = slope * d / D
print('\nwavelength (m) =', wavelength)
print('wavelength (nm) =', wavelength * 1e9)


"""
x_n vs n
"""
n = [-2, -1, 1, 2]
x_n = [-0.122, -0.105, -0.070, -0.055]

regression_res = stats.linregress(n, x_n)
slope = regression_res.slope
intercept = regression_res.intercept
slope_stderr = regression_res.stderr
intercept_stderr = regression_res.intercept_stderr
r = regression_res.rvalue

bestfitline = list(map(linefunc, n))

plt.scatter(n, x_n)
plt.xlabel('n')
plt.ylabel('$x_n (m)$')
plt.title('Single Slit Envelope')
plt.plot(n, bestfitline, color='red')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.25)
plt.show()

print('\nsingle slit envelope')
print('r =', r)
print('slope =', slope)
print('\tslope_error =', slope_stderr)
print('intercept =', intercept)
print('\tintercept_error =', intercept_stderr)

wavelength = 650 * 1e-9
a = 1 / slope * wavelength * D
print('a(m) =', a)
