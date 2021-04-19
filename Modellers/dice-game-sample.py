import random as rd
seed = int(input())
rd.seed(seed)

numero = 0
jogadas_feitas = 0
while numero != 6:
    numero = rd.randint(1, 6)
    jogadas_feitas += 1
else:
    print(jogadas_feitas)
