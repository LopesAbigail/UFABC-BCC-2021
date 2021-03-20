# Retornando media ponderada em coluna criada
import pandas as pd
df = pd.read_csv("fake-classrooms15.csv")
df["Ponderada"] = 5*(df["Prova 1"] + df["Prova 2"])
print(df)
