# Ler o nome de duas colunas da tabela - col1: var independente (X) e col2 (Y) var dependente
# Calcular e imprimir a correlacao entre as duas colunas
# Calcular e mostrar a equacao da reta na forma y = ax + b
# Ler um numero inteiro x representando um valor de col1 que sera usado para fazer a predicao
# Se correlacao < 0.39, exibir a mensagem "Correlação < 0.39. Predição não exibida!"
# Se correlacao >= 0.79, calcular e imprimir o valor de y (predicao) e a mensagem "Correlação >= 0.79"
# Se correlacao >= 0.39 e < 0.79 calcular e imprimir o valor de y e a mensagem "Correlação < 0.79. Atenção com a predição!"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://www.dropbox.com/s/s108a7yp3whqtf8/fake-classrooms-correl09.csv?dl=1")

col_1 = input()
col_2 = input()
correlacao_cols_1_2 = df[col_1].corr(df[col_2])
# Reta
(a, b) = np.polyfit(x=df[col_1], y=df[col_2], deg=1)
# X para predicao
x = int(input())
predicao = a*x+b

print("Correlação entre " + col_1 + " e " +
      col_2 + " = %.2f" % (correlacao_cols_1_2))
print("Equação: y = %.2fx + %.2f" % (a, b))
print("Predição de " + col_1 + " para " +
      col_2 + " = %.2f é %.2f." % (x, predicao))

if correlacao_cols_1_2 < 0.39:
    print("Correlação < 0.39. Predição não exibida!")
elif correlacao_cols_1_2 >= 0.79:
    print("Correlação >= 0.79.")
else:
    print("Correlação < 0.79. Atenção com a predição!")

# Grafico
plt.plot(df[col_1], df[col_2], '.')
# reta
dir_x = np.arange(0, 9)
dir_y = a*dir_x+b
plt.xlabel(col_1)
plt.ylabel(col_2)
plt.title(col_1+".correl("+col_2+")")
plt.plot(dir_x, dir_y, 'r')
