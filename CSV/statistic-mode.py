# Retornando a moda
import pandas as pd
df = pd.read_csv("fake-classrooms18.csv")
print(df["Prova 1"].mode())
