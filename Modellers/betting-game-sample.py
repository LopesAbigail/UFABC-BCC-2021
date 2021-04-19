import random as rd
seed = int(input())
rd.seed(seed)

saldo = 120
aposta = 20
jogada = 1
while (saldo > 0 and saldo < 240):
    sorteio = rd.randint(1, 3)
    if sorteio == 1:
        saldo = saldo+40
        print("Ganhou 40 reais")
    else:
        saldo = saldo-aposta
        print("Perdeu 20 reais")
    jogada += 1

print("O jogador tem", saldo, "reais")
