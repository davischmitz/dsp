
import matplotlib.pyplot as plt
import numpy as np

# implementação da função abs do python, calcula o valor absoluto dos elementos complexos do array z
def magn(z):
    return ((z.real**2 + z.imag**2)*(1/2))

Fs = 1500  # taxa de amostragem
Ts = 1.0 / Fs  # periodo de amostragem

# arange cria um array com valores igualmente espaçados dentro de um intervalo especificado
t = np.arange(0, 1, Ts)  # vetor de tempo que represente o tempo de amostragem do sinal que será analisado pela DFT

f1 = 100  # frequencia do sinal 1
x1_n = np.sin(2 * np.pi * f1 * t + 0)

f2 = 600  # frequencia do sinal 2
x2_n = np.sin(2 * np.pi * f2 * t + np.pi)

x_n = x1_n + x2_n

n = len(x_n)  # tamanho do sinal
k = np.arange(n)  # vetor em k
T = n / Fs

frq = k / T  # os dois lados do vetor de frequencia
frq = frq[range(int(n/2))]  # apenas um lado

X = np.zeros(int(n/2), dtype=np.complex64)

for m in range(0, int(n/2)):
    mysumm = 0
    for nn in range(0, n):
        mysumm += x_n[nn] * (np.cos(2 * np.pi * nn * m / n) - 1j * np.sin(2 * np.pi * nn * m / n))
    X[m] = mysumm

fig, ax = plt.subplots(4, 1)
ax[0].plot(t, x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq, magn(X), 'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')

X = np.fft.fft(x_n)/n # cálculo utilizando a fft do numpy para comparação
X = X[range(int(n/2))]
ax[2].plot(t, x_n)
ax[2].set_xlabel('Tempo')
ax[2].set_ylabel('Amplitude')
ax[3].plot(frq, magn(X), 'r')
ax[3].set_xlabel('Freq (Hz)')
ax[3].set_ylabel('|X(freq)|')

plt.show()
