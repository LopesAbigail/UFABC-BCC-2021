import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/cwfdaqzzznaetiz/fake-file02.csv?dl=1", sep=",", decimal=",")

print('%.2f' % df["Funcionario"].max())
