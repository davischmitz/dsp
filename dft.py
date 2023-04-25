"""
Created on 2023

Aline Nunes e Davi Souza

Implementação de um somatório de DFT  e comparação com uma fft do numpy

DFT (Discrete Fourier Transform): operação que converte um sinal de domínio do tempo em seu correspondente espectro de frequência.
- Cálculo: decomposição de um sinal discreto em uma soma ponderada de funções sinusoidais complexas com frequências discretas
- fórmula geral: X[k] = somatório de (x[n] * exp(-2pijkn/N))
onde x[n] é o sinal de entrada, X[k] é o valor da DFT no índice k, N é o tamanho do sinal e j é a unidade imaginária (j² = -1)
- Propriedade de simetria conjugada: os valores da transformada para frequências acima da metade do limite superior do sinal são espelhados em relação à metade inferior.

FFT (Fast Fourier transform): algoritmo que computa a DFT de forma mais eficiente do que a implementação direta da fórmula da DFT.

Critério de Nyquist: fs > 2 * fmax
"""

import matplotlib.pyplot as plt
import numpy as np

# implementação da função abs do python, calcula o valor absoluto dos elementos complexos do array z
def magn(z):
    return (z.real**2 + z.imag**2)**(1/2)

Fs = 1500  # taxa de amostragem
Ts = 1.0 / Fs  # periodo de amostragem

# arange cria um array com valores igualmente espaçados dentro de um intervalo especificado
# vetor de tempo que represente o tempo de amostragem do sinal que será analisado pela DFT
t = np.arange(0, 1, Ts)

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

# calcula a DFT de um sinal discreto x_n de tamanho n, utilizando a abordagem direta de somatórios
# calcula os valores da DFT nos índices m que variam de 0 a n/2-1, a "metade positiva" da DFT
for m in range(0, int(n/2)): # percorre os valores de m que variam de 0 a n/2-1: está percorrendo apenas a metade positiva da DFT, e os valores para a metade negativa são calculados usando a simetria conjugada complexa 
    mysumm = 0
    for nn in range(0, n): # para cada valor de m, é calculada a soma ponderada de x_n com as funções senoidais e cossenoidais correspondentes a essa frequência m
        mysumm += x_n[nn] * (np.cos(2 * np.pi * nn * m / n) -
                             1j * np.sin(2 * np.pi * nn * m / n)) # para cada valor de n, é calculada a contribuição da função senoidal e cossenoidal correspondente a essa frequência m, usando as funções np.cos e np.sin
    X[m] = mysumm # valor resultante da soma ponderada é atribuído ao índice m do vetor de saída X, que contém os valores calculados da DFT

fig, ax = plt.subplots(4, 1)
ax[0].set_title('DFT')
ax[0].plot(t, x_n)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq, 2 * magn(X/n), 'r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|X(freq)|')

X = np.fft.fft(x_n)/n  # cálculo utilizando a fft do numpy para comparação
X = X[range(int(n/2))]

ax[2].set_title('FFT')
ax[2].plot(t, x_n)
ax[2].set_xlabel('Tempo')
ax[2].set_ylabel('Amplitude')
ax[3].plot(frq, 2 * abs(X), 'r')
ax[3].set_xlabel('Freq (Hz)')
ax[3].set_ylabel('|X(freq)|')

plt.show()
