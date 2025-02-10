# x^3-x+1 = 0, x^3-x^2-9x-9 = 0, x^2-e^x =0, 5x-6ln(x)-7 = 0, cos(x)+2x-3 = 0

import matplotlib.pyplot as plt
import numpy as np
from math import e

unsolved = True
eps = 0.01
def f(x):
    return (5*x-6*np.log1p(x-1)-7)

print('Enter minimum of x:', end=' ')
a = float(input())
a1 = a
print('Enter maximum of x:', end=' ')
b = float(input())
b1 = b

x = np.linspace(a, b, 100)
y = f(x)
while unsolved:
    c = (a+b)/2
    if f(c)*f(a) < 0:
        b = c
    else:
        a = c
    if abs((b-a))/2 <= eps:
        if round(c, 1) == (a, b):
            print('No solutions in interval [', a1, ' , ', b1, ']', ', or x = ', a1, ' or ', b1, sep='')
            secondroot = False
        print(c)
        unsolved = False
        secondroot = True

while secondroot:
    c1 = (a1 + b1) / 2
    if f(c1) * f(b1) <= 0:
        a1 = c1
    else:
        b1 = c1
    if abs((b1 - a1)) / 2 <= eps:
        if round(c, 1) != round(c1, 1):
            print(c1)
        secondroot = False

plt.plot(x, y)
plt.plot(x, np.zeros(len(x)))
plt.show()
