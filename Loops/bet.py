# o jogador para de jogar se: atinge saldo 260, fica com saldo zero ou negativo ou se completou 13 rodadas (independente de seu saldo)

import random as rd
seed = int(input())
rd.seed(seed)

saldo = 100
aposta = 20
jogada = 1
while (jogada <= 13 and saldo > 0):
    sorteio = rd.randint(1, 2)
    if sorteio == 1:
        saldo = saldo+aposta
        print("Ganhou", aposta, "reais")
    else:
        saldo = saldo-aposta
        print("Perdeu", aposta, "reais")
    jogada += 1

print("O jogador tem", saldo, "reais")
