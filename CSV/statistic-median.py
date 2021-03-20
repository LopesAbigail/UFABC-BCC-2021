# Retornando a mediana
import pandas as pd
df = pd.read_csv("fake-classrooms06.csv")
print("%.2f" % df["Prova 2"].median())
