# Ler a planilha
# Receber do usuario o nome de uma coluna da planilha (que deve ser Exame 2 ou Exame 3)
# Calcula a correlacao entre a coluna recebida e a coluna Exame 1
# Imprimir a correlacao com duas casas decimais

import pandas as pd

df = pd.read_csv("Exames3.csv")

# lendo a coluna - "Entre com a coluna desejada (Exame 2 ou Exame 3):"
coluna_lida = input()

if (coluna_lida == "Exame 2" or coluna_lida == "Exame 3"):
    nota_final = df["Exame 1"]
    # Correlacao entre coluna recebida e coluna "Exame 1"
    correlacao = df[coluna_lida].corr(df["Exame 1"])
    print('%.2f' % correlacao)
else:
    print("Coluna inválida!")
