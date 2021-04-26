# Prova Final - ex02

import pandas as pd

#df = pd.read_csv("fake-classrooms28.csv")
df = pd.read_csv(
    "https://www.dropbox.com/s/aze7tzz24jhp0d8/fake-classrooms28.csv?dl=1")

indice_aluno = int(input())

nome, prova1, prova2, trabalho = df[[
    "Nome", "Prova 1", "Prova 2", "Trabalho"]].loc[indice_aluno]
media = (prova1 + prova2 + trabalho)/3

if media >= 8.6:
    conceito = "A"
else:
    if media >= 7.1:
        conceito = "B"
    else:
        if media >= 5.9:
            conceito = "C"
        else:
            if media >= 4:
                conceito = "D"
            else:
                conceito = "F"
print("Nome:", nome)
print("Prova 1:", prova1)
print("Prova 2:", prova2)
print("Trabalho:", trabalho)
print("Media: %.2f" % (media))
print("Conceito:", conceito)
