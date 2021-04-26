# Prova Final - ex05

x = int(input())
y = int(input())
multiplos_3 = 0
for i in range(x, y+1):
    if i % 3 == 0:
        print("Múltiplo de 3")
        multiplos_3 += 1
    else:
        print(i)
print("Total de múltiplos de 3:", multiplos_3)
