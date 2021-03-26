# Ler planilha do link: https://www.dropbox.com/s/lp2xto2f9p424ku/fake-classrooms-correl08.csv?dl=1
# Ler uma das colunas da tabela (Faltas ou Horas Estudo)
# Calcular e imprimir o coeficiente de determinacao entre a coluna Nota Final e a coluna lida

import pandas as pd
import numpy as np

df = pd.read_csv("fake-classrooms-correl08.csv")

coluna_lida = input()
if(coluna_lida == "Faltas" or coluna_lida == "Horas Estudo"):
    # formula para correlacao linear
    ccor = df[coluna_lida].corr(df['Nota Final'])
    cdet = ccor**2  # coeficiente de determinacao
    print('%.2f' % cdet)
else:
    print("Coluna inválida")
