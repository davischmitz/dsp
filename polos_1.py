# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:10:18 2019

@author: jeans
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

N = 20;
b = [1, 0];
#Valores para p: 0.9, 0.6, 1.1, -0.8, -0.4 e -1.2
p = -0.4;
a = [1, -p];
x = np.zeros(N);
x[0] = 1;
y = signal.lfilter(b, a, x);
#y = filter(b, a, x);
plt.plot(y)