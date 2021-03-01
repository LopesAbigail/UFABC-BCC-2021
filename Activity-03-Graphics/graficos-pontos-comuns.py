import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.arange(-5, 2.1, 0.1)
y1 = np.cos(x)
y2 = 1 - np.sqrt(1 - (x-1)**2)
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Pontos em comum entre duas funções")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
