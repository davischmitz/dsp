# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:40:09 2019

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

p = 0.9*np.exp(1j*np.pi/10)
a = np.poly([p, np.conj(p)])
b = [1, 0, 0]
theta = np.arange(0, 2*np.pi, np.pi/100)
c = np.exp(1j*theta)
plt.plot(c.real, c.imag)

zvals = np.roots(b)
pvals = np.roots(a)
plt.plot(pvals.real, pvals.imag, 'X')
plt.plot(zvals.real, zvals.imag, 'o')

plt.figure(2)
N = 40
x = np.zeros(N)
x[0] = 1

plt.subplot(2, 3, 1)
p = 0.9*np.exp(-1j*np.pi/10)
a = np.poly([p, np.conj(p)])

# Variaveis de estado
xh1 = 0
xh2 = 0
yh1 = 0
yh2 = 0

a1 = -a[1]
a2 = -a[2]
y = np.zeros(N)

for n in range(0, N):
    y[n] = x[n]+a1*yh1+a2*yh2
    yh2 = yh1
    yh1 = y[n]

plt.stem(y)
plt.title('0.9, pi/10')

plt.subplot(2, 3, 2)
p = 1*np.exp(-1j*np.pi/10)
a = np.poly([p, np.conj(p)])

# Variaveis de estado
xh1 = 0
xh2 = 0
yh1 = 0
yh2 = 0

a1 = -a[1]
a2 = -a[2]
y = np.zeros(N)

for n in range(0, N):
    y[n] = x[n]+a1*yh1+a2*yh2
    yh2 = yh1
    yh1 = y[n]

plt.stem(y)
plt.title('1, pi/10')

plt.subplot(2, 3, 3)
p = 1.2*np.exp(-1j*np.pi/10)
a = np.poly([p, np.conj(p)])

# Variaveis de estado
xh1 = 0
xh2 = 0
yh1 = 0
yh2 = 0

a1 = -a[1]
a2 = -a[2]
y = np.zeros(N)

for n in range(0, N):
    y[n] = x[n]+a1*yh1+a2*yh2
    yh2 = yh1
    yh1 = y[n]

plt.stem(y)
plt.title('1.2, pi/10')

plt.subplot(2, 3, 4)
p = 1*np.exp(-1j*np.pi/4)
a = np.poly([p, np.conj(p)])

# Variaveis de estado
xh1 = 0
xh2 = 0
yh1 = 0
yh2 = 0

a1 = -a[1]
a2 = -a[2]
y = np.zeros(N)

for n in range(0, N):
    y[n] = x[n]+a1*yh1+a2*yh2
    yh2 = yh1
    yh1 = y[n]

plt.stem(y)
plt.title('-1, pi/4')

plt.subplot(2, 3, 5)
p = 1*np.exp(-1j*np.pi/2)
a = np.poly([p, np.conj(p)])

# Variaveis de estado
xh1 = 0
xh2 = 0
yh1 = 0
yh2 = 0

a1 = -a[1]
a2 = -a[2]
y = np.zeros(N)

for n in range(0, N):
    y[n] = x[n]+a1*yh1+a2*yh2
    yh2 = yh1
    yh1 = y[n]

plt.stem(y)
plt.title('-1, pi/2')

plt.subplot(2, 3, 6)
p = 1*np.exp(-1j*np.pi/20)
a = np.poly([p, np.conj(p)])

# Variaveis de estado
xh1 = 0
xh2 = 0
yh1 = 0
yh2 = 0

a1 = -a[1]
a2 = -a[2]
y = np.zeros(N)

for n in range(0, N):
    y[n] = x[n]+a1*yh1+a2*yh2
    yh2 = yh1
    yh1 = y[n]

plt.stem(y)
plt.title('-1, pi/20')
plt.show()
