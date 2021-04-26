# Prova Final - ex01

import random as rd

seed = int(input())
rd.seed(seed)

saldo_inicial = float(input())
saldo = saldo_inicial
valor_apostado = int(input())
numero_apostado = 5  # sempre aposta em 5
quantidade_execucao = int(input())

faliu = 0
prosperou = 0
status = ""

for i in range(0, quantidade_execucao):
    saldo = saldo_inicial
    while saldo >= 0 and saldo <= 2*saldo_inicial:
        sorteio = rd.randint(5, 6)
        if sorteio == numero_apostado:
            saldo = saldo+valor_apostado
        else:
            saldo = saldo-valor_apostado
    if saldo < 0:
        faliu = faliu+1
    else:
        prosperou = prosperou+1

print("O jogador faliu", faliu, "vezes")
print("O jogador prosperou", prosperou, "vezes")
if faliu < prosperou:
    status = "menor"
else:
    status = "maior"
print("O número de vezes que o jogador faliu eh",
      status, "que o numero de vezes que prosperou")
