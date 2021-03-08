import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/gs16ryvchrtwlb3/fake-file10.csv?dl=1", sep=",")

print(df[["Idade", "Meses", "Funcionario", "Genero"]].query(
    "Idade <= 49 and Meses < 56"))
