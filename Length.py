# Пусть горка имеет форму, которую можно описать формулами:
# 1) cos(x)
# (0.001**2 + (cos(eps) - cos(eps-0.001))**2)**0.5
# 2) cos(x) + 0.1*x2
# (0.001**2+(cos(eps)+0.1*eps**2 - (cos(eps-0.001)+0.1*(eps-0.001)**2))**2)**0.5
# 3) -tanh(x-π/2)
# (0.001**2+(-tanh(eps-pi/2)+ tanh(eps-0.001-pi/2))**2)**0.5
# 4) -0.2*(x- π)3 + 0.5*(x- π)2 +1
#(0.001**2+((-0.2*(eps-pi)**3+0.5*(eps-pi)**2-1) - (-0.2*(eps-0.001-pi)**3+0.5*(eps-0.001-pi)**2-1))**2)**0.5
# На отрезке от 0 до π. Найти длину этих горок

import numpy as np
import matplotlib.pyplot as plt
from math import pi, cos, tanh

def f(x):
    return -0.2*(x- pi)**3 + 0.5*(x- pi)**2 +1

x = np.linspace(0, pi, 200)
y = f(x)
eps = 0
l = 0

while eps <= pi:
    eps += 0.001
    l += (0.001**2+  (f(eps) - f(eps-0.001))**2)**0.5
print(l)
plt.plot(x, y)
plt.show()