# Receber do teclado duas colunas da tabela - coluna lida1 e coluna lida2
# Exibir a media de valores da coluna lida1, a media de valores da coluna lida2 e uma mensagem que pode ser:
# Apenas Media coluna_lida1 eh maior que 5.7
# Apenas Media coluna_lida2 eh maior que 5.7
# As duas Medias sao maiores que 5.7
# Nenhuma das medias eh maior que 5.7

import pandas as pd

df = pd.read_csv(
    "https://www.dropbox.com/s/tkrs8wdr6y6oa4x/fake-classrooms27.csv?dl=1")

coluna_lida1 = input()
coluna_lida2 = input()
media_coluna_lida1 = df[coluna_lida1].mean()
media_coluna_lida2 = df[coluna_lida2].mean()

print("Media " + coluna_lida1 + " = %.2f" % (media_coluna_lida1))
print("Media " + coluna_lida2 + " = %.2f" % (media_coluna_lida2))

if media_coluna_lida1 > 5.7:
    if media_coluna_lida2 > 5.7:
        print("As duas Medias sao maiores que 5.7")
    else:
        print("Apenas Media " + coluna_lida1 + " eh maior que 5.7")
elif media_coluna_lida2 > 5.7:
    print("Apenas Media " + coluna_lida2 + " eh maior que 5.7")
else:
    print("Nenhuma das medias eh maior que 5.7")
