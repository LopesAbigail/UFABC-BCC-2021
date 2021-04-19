import random as rd
seed = int(input())
rd.seed(seed)
quantidade_execucao = int(input())
soma_sorteios_feitos = 0
media_sorteios_feitos = 0

for i in range(0, quantidade_execucao):
    soma_valores_aleatorios = 0
    quantidade_sorteios_feitos = 0
    while soma_valores_aleatorios < 1:
        quantidade_sorteios_feitos = quantidade_sorteios_feitos+1
        valor_aleatorio = rd.random()
        soma_valores_aleatorios = soma_valores_aleatorios+valor_aleatorio
    soma_sorteios_feitos += quantidade_sorteios_feitos
media_sorteios_feitos = soma_sorteios_feitos / quantidade_execucao
print("%.4f" % media_sorteios_feitos)
