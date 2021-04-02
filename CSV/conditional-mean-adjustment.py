# Ler o link da planilha
# Receber do usuario o nome de um dos exames (Exame 1, Exame 2,...)
# Adicionar uma nova coluna com nome Ajuste com as notas do exame recebido no passo anterior, ajustadas de acordo com as seguintes regras:
# • Se a media do exame for < 50, a nota ajustada tera um acrescimo de 20% da nota original
# • Se a media do exame estiver em [50, 70), a nota ajustada tera um acrescimo de 10% da nota original
# • Se a media do exame estiver em [70, 80), a nota ajustada tera um acrescimo de 5% da nota original
# • Caso contrario, nao ha nenhum ajuste (a coluna Ajuste ainda deve ser criada, mas com os mesmos valores obtidos no exame).
# Imprimir a planilha completa

import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/kwibw8umms9yh9w/NotasAjuste.csv?dl=1")

nome_exame = input()
media = df[nome_exame].mean()

if media < 50:
    df["Ajuste"] = 1.2*df[nome_exame]
elif media < 70:
    df["Ajuste"] = 1.1*df[nome_exame]
elif media < 80:
    df["Ajuste"] = 1.05*df[nome_exame]
else:
    df["Ajuste"] = df[nome_exame]

print(df)
