#Это моя лабораторная работа, в которой нужно было сделать апроксимацию.
# Данные экспериментальные!

import  matplotlib.pyplot as plt
import numpy as np
from math import pi

sumx, sumy, sumx2, sumxy = 0, 0, 0, 0
l = np.array([1.26, 1.26, 1.26, 0.895, 0.895, 0.895, 0.895, 0.77, 0.77, 0.77, 0.77, 0.5, 0.5, 0.3, 0.3 ])
l = np.array(4*pi**2/l)
t = np.array([2.17, 2.17, 2.23, 1.9, 1.9, 1.9, 1.91, 1.75, 1.76, 1.77, 1.82, 1.47, 1.4, 1.05, 1.09])

# ax+b = y
for i in range(0, 15):
    sumxy += l[i]*t[i]
    sumx += l[i]
    sumy += t[i]
    sumx2 += l[i]**2

a = (15*sumxy - sumx*sumy)/(15*sumx2-(sumx)**2)
b = (sumy - a*sumx)/15

y = a*l + b
print(a)
plt.scatter(l, t)
plt.plot(l, y, c='r')
plt.show()