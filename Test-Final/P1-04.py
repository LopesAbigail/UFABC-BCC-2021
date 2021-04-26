# Prova Final - ex04

import pandas as pd
import numpy as np

# df = pd.read_csv("fake-classrooms-correl04.csv")
df = pd.read_csv("https: // www.dropbox.com/s/e4zjndhy7v6l3un/fake-classrooms-correl04.csv?dl=1)

var_indep_x = input()

if var_indep_x == "Faltas" or var_indep_x == "Horas Estudo":
    predicao_nota_final = float(input())
    (a, b) = np.polyfit(x=df[var_indep_x], y=df["Nota Final"], deg=1)
    valor = a*predicao_nota_final + b
    print("%.2f" % (valor))
