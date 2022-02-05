from sympy import *
from math import pi

wavelength, slope_double, slope_single, d, D, a = symbols('w md ms d D a')

s_w, s_md, s_ms, s_d, s_D, s_a = symbols('s_w s_md s_ms s_d s_D s_a')

init_printing(use_unicode=True)

wavelength = slope_double * d / D

a = 1 / slope_single * wavelength * D

d_wavelength = wavelength * sqrt((s_md / slope_double) ** 2 + (s_d / d) ** 2 + (s_D / D) ** 2)

d_a = a * sqrt((s_ms / slope_single) ** 2 + (s_w / wavelength) ** 2 + (s_D / D) ** 2)

vals = {slope_double: -9.57 * 10**-4, slope_single: 1.69 * 10**-2, d: 2.5 * 10**-4, D: 0.99, \
    s_md: 2.79 * 10**-4, s_ms: 3.08 * 10**-4, s_d: 10**-5, s_D: 0.01}

print('\ndouble slit')
print('wavelength =', wavelength.evalf(subs=vals))
print('error wavelength =', d_wavelength.evalf(subs=vals))

vals[wavelength] = wavelength.evalf(subs=vals)
vals[s_w] = d_wavelength.evalf(subs=vals)

print('\nsingle slit')
print('a 1 =', a.evalf(subs=vals))
print('error a 1 =', d_a.evalf(subs=vals))

new_wavelength, new_s_w = symbols('new_wavelength s_w_new')
vals[new_wavelength] = 6.5 * 10**-7
vals[new_s_w] = 10**-9

a2 = 1 / slope_single * new_wavelength * D
d_a2 = a * sqrt((s_ms / slope_single) ** 2 + (new_s_w / new_wavelength) ** 2 + (s_D / D) ** 2)

print('a 2 =', a2.evalf(subs=vals))
print('error a 2 =', d_a2.evalf(subs=vals))

signal, noise, s_sig, s_noise = symbols('signal noise s_sig s_noise')
signal_noise_ratio = signal / noise
d_snr = signal_noise_ratio * sqrt((s_sig / signal) ** 2 + (s_noise / noise) ** 2)
vals={signal:1626.58, noise: 16.37, s_sig: 0.10, s_noise: 0.10}
print('\nsignal noise ratio =', signal_noise_ratio.evalf(subs=vals))
print('error signal noise ratio =', d_snr.evalf(subs=vals))
