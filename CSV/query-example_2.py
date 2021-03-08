import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/flhgro4kxw1c1yr/fake-file03.csv?dl=1", sep=",")

print(df.query("Idade < 43"))
