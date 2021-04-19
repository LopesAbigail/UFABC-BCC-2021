import random as rd
seed = int(input())
rd.seed(seed)

# não modifique as linhas acima, pois elas serão usadas pelo corretor automático
# Para testar aqui, no Notebook, digite um número qualquer para seed
# continue seu código a partir daqui
n = int(input())
somatorio_r = 0

for i in range(0, n):
    s = 0
    r = 0
    while s < 1:
        r = r+1
        x = rd.random()
        s = s+x
    somatorio_r += r
media = somatorio_r / n
print("%.4f" % media)
