# Ler a planilha do link https://www.dropbox.com/s/zex7e9w1obxoit7/Exames2_versao4.csv?dl=1
# Considerar Exame 1 o eixo x e Exame 2  o eixo y
# Calcular o polinomio de grau 2 (ax2 + bx + c) que melhor se encaixa aos dados
# Imprimir os valores de a, b e c desse polinomio (um por linha e apenas o numero, com 2 casas decimais)
# Fazer o grafico de dispersao e incluir o polinomio obtido (para x de 0 a 100) [sem incluir essa parte do codigo na submissao!]
# Nos graficos deste link: https://www.dropbox.com/s/zpgj0er0s2bp25k/Graficos.pdf?dl=0 Verificar qual numero de grafico e mais parecido com o obtido
# Imprimir o numero (apenas o numero da resposta)

import pandas as pd
import numpy as np

df = pd.read_csv("Exames2_versao4.csv")

# grafico de dispersao
# plt.plot(df["Exame 1"],df["Exame 2"],'.')
# polinomio de grau 2
(a, b, c) = np.polyfit(x=df["Exame 1"], y=df["Exame 2"], deg=2)

# coeficientes a, b e c
print('%.2f' % a)
print('%.2f' % b)
print('%.2f' % c)

# polinomio obtido
# x = np.arange(0,100,0.2)
# y = a*x**2+b*x+c
# plt.plot(x,y,'r')
print(1)
