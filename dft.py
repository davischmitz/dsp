import numpy
import matplotlib.pyplot as plt


def naive_DFT(x):
    N = numpy.size(x)
    X = numpy.zeros((N,), dtype=numpy.complex128)
    for m in range(0, N):
        for n in range(0, N):
            X[m] += x[n]*numpy.exp(-numpy.pi*2j*m*n/N)
    return X


x = numpy.random.rand(1024,)
# compute DFT
X = naive_DFT(x)
# compute FFT using numpy's fft function
X2 = numpy.fft.fft(x)
# now compare DFT with numpy fft

plt.subplot(221)
plt.plot(x)
plt.subplot(222)
plt.plot(X2)

plt.show()
