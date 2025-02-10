# Пусть кляксы на бумаге имеют следующие формы. Найти их площади.
# 1) y1(x) = sin(2*x)+1
# y2(x) = -0.2*x^2+0.5
# [0, pi]
# 2) y1(x) = cos(x) +1.2
# y2(x) = -0.5x^2+0.7
# [-pi/2, pi/2]
# 3) y1(x) = e^(-x^2) + 1
# y2(x) = -0.3*x^3 +0.5
# [-2,2]
# 4) y1(x) = e^(-x^2) +0.5
# y2(x) = 0.2*sin(3*x)-0.5
# [-2, 2]
# y1(x) = e^-((x+1)^2) + e^-((x-1)^2) +0.5
# y2(x) = -0.3*x^2
# [-2,2]

import numpy as np
import matplotlib.pyplot as plt
from math import pi, e

a = -2
b = 2
eps = a
s1, s2 = 0, 0

def f1(x):
    return e**(-(x+1)**2) + e**(-(x-1)**2) + 0.5
def f2(x):
    return -0.3*x**2

x = np.linspace(a, b, 200)
y1 = f1(x)
y2 = f2(x)

while eps <= b:
    s1 += f1(eps)*0.001
    s2 += f2(eps)*0.001
    eps += 0.001
s = abs(s1 - s2)
print(s)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()