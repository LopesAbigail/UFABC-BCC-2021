# Ler a planilha do link
# Considerar: Exame 2 o eixo x e Exame 1 o eixo y
# Calcular o polinomio de grau 3 que melhor se encaixa aos dados
# Receber do usuario um numero inteiro n;
# Utilizar o polinomio para calcular a predicao do valor da coluna Exame 1 quando o valor da coluna Exame 2 for n
# Imprimir a resposta com duas casas decimais

import pandas as pd
import numpy as np

df = pd.read_csv("Exames3_versao2.csv")

# obtendo os coeficientes da curva
(a, b, c, d) = np.polyfit(x=df["Exame 2"], y=df["Exame 1"], deg=3)
# polinomio que melhor se encaixa: a*x**3+b*x**2+c*x+d
n = int(input())
# predicao do valor do Exame 1 com base no valor do Exame 2
predicao_exame1 = a*n**3+b*n**2+c*n+d
print('%.2f' % predicao_exame1)
