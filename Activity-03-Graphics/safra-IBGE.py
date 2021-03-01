import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x = np.arange(0, 12, 1)
y = 8 + 5 * np.cos((np.pi*x - np.pi)/6)
plt.plot(x, y)
plt.title("Safra - IBGE")
plt.grid()
plt.xlabel("Mês")
plt.ylabel("Preço do produto X")
