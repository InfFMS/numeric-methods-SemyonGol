# У нас есть две среды с разными показателями преломления n1 и n2.
# Луч пускают из одной среды из точки с координатами (a,b).
# Под каким углом надо пустить луч, чтобы его оптическая длина пути была минимальной.
# n1*sin(a1) = n2*sin(a2)

import matplotlib.pyplot as plt
import numpy as np
from math import pi, sqrt, asin, degrees

def f(x):
    return (1-x**2)**0.5
# x1 = 2
# x2 = 2
# y1 = 2
# y2 = -2
# n1 = 1
# n2 = 1

print('Enter x1 coordinate:', end=' ')
x1 = float(input())
print('Enter y1 coordinate:', end=' ')
y1 = float(input())
print('Enter x2 coordinate:', end=' ')
x2 = float(input())
print('Enter y2 coordinate:', end=' ')
y2 = float(input())
print('Enter first refractive index:', end=' ')
n1 = float(input())
print('Enter second refractive index:', end=' ')
n2 = float(input())

ly = abs(y1-y2)
lx = abs(x1-x2)
sinA = np.linspace(0, 1, 300)
sinB = (sinA*n1)/n2
k1 = sinA + f(sinA)
k2 = sinB + f(sinB)
l1 = np.linspace(y1, sqrt(ly**2+lx**2), 300)        #объяснения в файле img.png
l2 = (lx+ly-k1*l1)/k2
l = abs(l1 + l2)                                         #почему-то код работает не так, как
print((min(l)))                                          #запланированно. Помогите, тыкните
for i in range(0, len(l)):                               #в проблему. Теоретически всё верно,
    if l[i] == min(l):                                   #но получается так, что есть более
        msinA = sinA[i]                                  #короткое расстояние, чем прямая. Спасибо

print('Least angle with specified parameters:', degrees(asin(msinA)))

Ox1 = np.linspace(x1, x2, 10)
Oy1 = np.zeros(10)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(Ox1, Oy1, c='r')
axs[0].scatter(x1, y1)
axs[0].scatter(x2, y2)
axs[1].plot(sinA, l)
plt.show()