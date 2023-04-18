# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:38:28 2020

@author: jeans
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import chirp

Fs = 44100;  # taxa de amostragem
Ts = 1.0/Fs; # periodo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo

x = chirp(t, f0=20, f1=20000, t1=1, method='linear');

fc = 5000;  #frequencia de corte

L = 0.000100
Cap = 0.000220
R = 1
d = ((L*Cap*np.power((2/Ts), 2)) + (R*Cap*(2/Ts)) + 1)

b0 = 1/d
b1 = 2*b0;
b2 = b0;

a0 = 1;
a2 = ((L*Cap*(np.power((2/Ts), 2))) - (R*Cap*(2/Ts) + 1)) / d
a1 = (((-2)*L*Cap*np.power((2/Ts), 2)) + 2) / d


#Variaveis de estado
xh1=0;
xh2=0;

yh1=0;
yh2=0;

y = np.zeros(len(x));

for n in range(0,len(x)):
    y[n]= b0*x[n] + b1*xh1 + b2*xh2 -a1*yh1 -a2*yh2;
    
    yh2=yh1;
    yh1=y[n];
    
    xh2=xh1;
    xh1=x[n];
    
n = len(y) # tamanho do sinal
k = np.arange(n) #vetor em k
T = n/Fs
frq = k/T # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))] # apenas um lado

Y = np.fft.fft(y)/n # calculo da fft e normalização por n
Y = Y[range(int(n/2))]

X = np.fft.fft(x)/n # calculo da fft e normalização por n
X = X[range(int(n/2))]

plt.subplot(3,1,1)
plt.plot(t,x)
plt.title('Sweep')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')

plt.subplot(3,1,2)
plt.plot(frq,abs(X),'r')
plt.title('Fourier - Sweep')
plt.xlabel('Freq (Hz)')
plt.ylabel('|X(freq)|')

plt.subplot(3,1,3)
plt.plot(frq,abs(Y),'r')
plt.grid(True, which="both")
plt.title('Fourier - Filtro')
plt.xlabel('Freq (Hz)')
plt.ylabel('|X(freq)|')
plt.show()