from sympy import *
h1_, h2_, h1, h2, h3, D, L, g = symbols('h1_ h2_ h1 h2 h3 D L g')
init_printing(use_unicode=True)
s_h1, s_h2, s_h1_, s_h2_, s_h3, s_D, s_L = symbols('s_h1 s_h2 s_h1_ s_h2_ s_h3, s_D, s_L')


v0 = sqrt(10/7 * g * (h2_ - h1_ + h1 - h2))

v0y = v0 * (h2 - h3)/L
v0x = v0 * D/L

t = (v0y + sqrt(v0y**2 + 2*g*h2)) / g

x = v0x * t

# these are all the variables x depends on
x_sigma = sqrt(\
(x.diff(h1) * s_h1) ** 2 + \
(x.diff(h2) * s_h2) ** 2 + \
(x.diff(h3) * s_h3) ** 2 + \
(x.diff(h1_) * s_h1_) ** 2 + \
(x.diff(h2_) * s_h2_) ** 2 + \
(x.diff(D) * s_D) ** 2 + \
(x.diff(L) * s_L) ** 2  \
)

v0_sigma = sqrt(\
(v0.diff(h1) * s_h1)**2 + \
(v0.diff(h2) * s_h2)**2 + \
(v0.diff(h1_) * s_h1_)**2 + \
(v0.diff(h2_) * s_h2_)**2 \
)
print(latex(v0_sigma))



trial_to_vals = { \
'plastic_1' : {g:981, h1_:121.2, s_h1_:0.2, h2_:116.4, s_h2_:0.2, h1:124.9, s_h1:0.2, h2: 113.9, s_h2:0.2, h3:105.8, s_h3:0.2, D:28.2, s_D:0.2, L:30.0, s_L:0.2}, \
'plastic_2' : {g:981, h1_:121.9, s_h1_:0.2, h2_:115.9, s_h2_:0.2, h1:132.6, s_h1:0.2, h2: 108.2, s_h2:0.2, h3:101.7, s_h3:0.2, D:27.7, s_D:0.2, L:30.3, s_L:0.2}, \
'metal_1' : {g:981, h1_:120.0, s_h1_:0.2, h2_:117.4, s_h2_:0.2, h1:125.6, s_h1:0.2, h2: 112.9, s_h2:0.2, h3:105.6, s_h3:0.2, D:27.5, s_D:0.2, L:29.3, s_L:0.2}, \
'metal_2' : {g:981, h1_:120.0, s_h1_:0.2, h2_:117.4, s_h2_:0.2, h1:129.5, s_h1:0.2, h2: 110.2, s_h2:0.2, h3:103.6, s_h3:0.2, D:28.4, s_D:0.2, L:29.6, s_L:0.2}
}

print(latex(x_sigma))
print(latex(x))

#print(latex(v0))
#print(latex(v0x))
#print(latex(v0y))
#print(latex(t))


for trial in trial_to_vals:
	print()
	vals = trial_to_vals[trial]
	print(trial)
	print('x_sigma = ', round(x_sigma.evalf(subs=vals), 2))
	print('x = ', round(x.evalf(subs=vals), 2))
