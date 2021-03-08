import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/gs16ryvchrtwlb3/fake-file10.csv?dl=1", sep=",")

print(df.sort_values(by="Salario", ascending=False))
