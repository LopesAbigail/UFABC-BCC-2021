# Sortear um valor de 1 a 4 - randint(1,4)
# Imprima a frase de acordo com o numero sorteado:
# 1: Doth mother know you weareth her drapes?
# 2: Rebellions are built on hope
# 3: I am no man
# 4: On your left

import random as rd
seed = int(input())
rd.seed(seed)
filmes = ["Doth mother know you weareth her drapes?",
          "Rebellions are built on hope", "I am no man", "On your left"]
#indicador_filme = rd.choice(filmes)
indicador_filme = rd.randint(1, 4)
if (indicador_filme > 0):
    print(filmes[indicador_filme-1])
