import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.arange(-2*np.pi, 5*np.pi/2, 0.1)
y1 = - abs(np.sin(x))
y2 = - abs(np.cos(x))
y3 = - np.sin(x)
y4 = abs(np.sin(x))
y5 = abs(np.cos(x))

plt.plot(x, y1, label='a')
plt.plot(x, y2, label='b')
plt.plot(x, y3, label='c')
plt.plot(x, y4, label='d')
plt.plot(x, y5, label='e')
plt.title("Comparação de funções")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
