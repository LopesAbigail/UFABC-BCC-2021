# Retornando o 41-esimo percentil
import pandas as pd
import numpy as np
df = pd.read_csv("fake-classrooms12.csv")
print("%.2f" % np.percentile(df["Trabalho"], q=41))
