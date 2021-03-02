import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.arange(36, 121.5, 1.5)
y1 = 99 + 21 * np.cos(2*np.pi*x)
y2 = 99 + 21 * np.cos(3*np.pi*x)
y3 = 78 + 42 * np.cos(x)
y4 = 78 + 42 * np.cos(3*np.pi*x)
y5 = 99 + 21 * np.cos(x)

#plt.plot(x, y1, label='a')
#plt.plot(x, y2, label='b')
plt.plot(x, y3, label='c')
plt.plot(x, y4, label='d')
# plt.plot(x, y5, label='e') nop
plt.title("Modelo - Pressão Arterial")
plt.grid()
plt.legend()
plt.xlabel("X - Tempo")
plt.ylabel("Y")
