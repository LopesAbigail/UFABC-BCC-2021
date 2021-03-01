# O sistema deve:
# 1. Receber a, b e c inteiros
# 2. Supor que c é o maior lado
# 3. Supor que a + b  > c
# 4. Imprimir "A", se triângulo for agudo
# 5. Imprimir "0", se triângulo for obtuso
 
a = int(input())
b = int(input())
c = int(input())

if a**2 + b**2 > c**2:
    print("A")
else:
    if a**2 + b**2 < c**2:
        print("O")
    else:
        print("R")
