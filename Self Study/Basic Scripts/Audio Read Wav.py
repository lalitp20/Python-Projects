import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
rate, data = wav.read('C:\Python Projects\Self Study\MySong.wav')
plt.plot(data)
plt.show()