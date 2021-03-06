from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1234)

fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time)
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

plt.clf()
plt.plot(time,x)
plt.show()

f, Pxx_den = signal.periodogram(x, fs)
#plt.semilogy(f, Pxx_den)
plt.plot(f, np.sqrt(Pxx_den))
plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()