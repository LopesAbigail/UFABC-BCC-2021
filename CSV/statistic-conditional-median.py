# Ler a planilha
# Receber do usuario a turma
# Calcular a media e a mediana da turma recebida no passo anterior
# Se a media for maior ou igual a mediana, imprima a palavra Media
# Caso contrario, imprima a palavra Mediana

import pandas as pd
import numpy as np

df = pd.read_csv(
    "https://www.dropbox.com/s/jqficiaig0a8aze/NotasTurmas.csv?dl=1")

turma = input()
turmas_validas = ["Turma 1", "Turma 2", "Turma 3", "Turma 4",
                  "Turma 5", "Turma 6", "Turma 7", "Turma 8", "Turma 9", "Turma 10"]

if turma in turmas_validas:
    if df[turma].mean() >= df[turma].median():
        print("Media")
    else:
        print("Mediana")
