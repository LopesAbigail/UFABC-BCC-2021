# Prova Final - ex03

import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/ztgwtiwucvkj8wx/simulacao1000.csv?dl=1")
# df = pd.read_csv("simulacao1000.csv")
coluna_correlacao = ""
coluna = input()

if coluna == "Pi" or coluna == "Erro":
    if coluna == "Pi":
        coluna_correlacao = "Erro"
    else:
        coluna_correlacao = "Pi"
    media_coluna = df[coluna].mean()
    desvio_padrao_coluna = df[coluna].std()
    correlacao = df[coluna].corr(df[coluna_correlacao])

print("Coluna =", coluna)
print("Media = %.6f" % (media_coluna))
print("Desvio padrao = %.6f" % (desvio_padrao_coluna))
print("Correlacao = %.6f" % (correlacao))
