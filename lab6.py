import numpy as np
from numpy import deg2rad
from math import sin, cos, sqrt

'''
R = 1.0974 * (10 ** 7)

def n_i(m, d, theta):
    return 2 / sqrt(1 - 4 * m / (R * d * sin(theta)))

def n_i(wavelength):
    return 2 / sqrt(1 - 4 / (R * wavelength))

# part 1: calibration of the grating
lambda_yellow = 587.56 * (10 ** -9)
theta_yellow = 20.95
d = lambda_yellow/sin(deg2rad(theta_yellow))
print('d =', d, 'm')

# part 2: Balmer series, initial energy
GB = 'greenish_blue'
PB = 'purple_blue'
RE = 'red'
angles = {1: {GB: 17.13333333, PB: 15.575, RE: 23.54166667}, \
    2: {GB: 36.26666667, PB: 31.88333333, RE: 52.95}}

lambda2color = {GB:None, PB:None, RE:None}
for color in [GB, PB, RE]:
    avg_lambda = 0
    for order in angles:
        curr_lambda = d * sin(deg2rad(angles[order][color])) / order
        avg_lambda += curr_lambda
    avg_lambda /= 2
    lambda2color[color] = avg_lambda
    print('\nlambda for color', color, ':', avg_lambda, 'm')

    curr_n_i = n_i(avg_lambda)
    print('n_i for color', color, ':', curr_n_i)
'''

from sympy import *

R = 1.0974 * (10 ** 7)

def n_i(wavelength):
    return 2 / sqrt(1 - 4 / (R * wavelength))

# part 1: calibration of the grating
lambda_yellow = 587.56 * (10 ** -9)
theta_yellow = 20.95
err_theta = deg2rad(1 / 60)
d = lambda_yellow/sin(deg2rad(theta_yellow))
print('d =', d, 'm')

err_d = d * cos(deg2rad(theta_yellow)) * err_theta / sin(deg2rad(theta_yellow))
print('err_d =', err_d, 'm')

# part 2: Balmer series, initial energy
GB = 'greenish_blue'
PB = 'purple_blue'
RE = 'red'
angles = {1: {GB: 17.13333333, PB: 15.575, RE: 23.54166667}, \
    2: {GB: 36.26666667, PB: 31.88333333, RE: 52.95}}

lambda2color = {GB:None, PB:None, RE:None}
for color in [GB, PB, RE]:
    avg_lambda = 0
    for order in angles:
        curr_lambda = d * sin(deg2rad(angles[order][color])) / order
        avg_lambda += curr_lambda
    avg_lambda /= 2
    lambda2color[color] = avg_lambda
    print('\nlambda for color', color, ':', avg_lambda, 'm')

    err_lambda = avg_lambda * sqrt((err_d / d) ** 2 + \
        (cos(deg2rad(angles[order][color])) * err_theta / sin(deg2rad((angles[1][color] + angles[2][color]) / 2))) ** 2)
    print('err lambda =', err_lambda, 'm')

    curr_n_i = n_i(avg_lambda)
    print('n_i for color', color, ':', curr_n_i)
    err_ni = -1 / ((1 - 4 / (R * avg_lambda)) ** 3/2) * 4 / (R * avg_lambda ** 2) * err_lambda
    print('err n_i =', err_ni)
