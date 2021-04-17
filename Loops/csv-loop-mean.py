# 1) Pede para o usuario digitar um numero n de planilhas
# 2) Para cada uma das planilhas, o programa deve:
# - Receber o link da planilha do usuario
# - Ler a planilha
# - Calcular o valor da funcao media da coluna D
# - Imprimir o valor com 2 casas decimais
import pandas as pd

nPlanilhas = int(input())
while (0 < nPlanilhas):
    link = input()
    df = pd.read_csv(link)
    print('%.2f' % df["D"].mean())
    nPlanilhas -= 1
