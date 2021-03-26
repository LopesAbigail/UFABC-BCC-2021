# Ler uma das demais colunas da tabela (Faltas ou Horas Estudo)
# Ler um numero x com duas casas decimais
# Calcular a equacao da reta de regressao linear f(x) = ax + b da coluna Nota Final (eixo y) com a coluna lida (eixo x)
# Dada esta equacao, calcular e imprimir o valor de f(x), em que x foi o numero lido anteriormente
import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms-correl10.csv")

# lendo a coluna - "Entre com a coluna desejada (Faltas ou Horas Estudo):"
coluna_lida = input()

if (coluna_lida == "Faltas" or coluna_lida == "Horas Estudo"):
    nota_final = df["Nota Final"]
    # valores de a e b para a reta de regressao linear
    (a, b) = np.polyfit(x=df[coluna_lida], y=nota_final, deg=1)
    # lendo valor n - "Insira um numero real de 2 casa decimais: "
    n = float(input())
    regressao_linear = a*n+b
    print('%.2f' % regressao_linear)
else:
    print("Coluna inválida!")
