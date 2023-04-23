X = np.fft.fft(x_n)/n # cálculo utilizando a fft do numpy para comparação
# X = X[range(int(n/2))]
# ax[2].plot(t, x_n)
# ax[2].set_xlabel('Tempo')
# ax[2].set_ylabel('Amplitude')
# ax[3].plot(frq, magn(X), 'r')
# ax[3].set_xlabel('Freq (Hz)')
# ax[3].set_ylabel('|X(freq)|')