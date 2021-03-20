# Retornar o desvio padrao
# Calculando a amplitude
#amplitude = df["Prova 2"].max()-df["Prova 2"]
# Calculando a variancia
#var = amplitude.var()
# A raiz quadrada da variancia eh o desvio padrao
import pandas as pd
df = pd.read_csv("fake-classrooms12.csv")
print("%.2f" % df["Prova 2"].std())
