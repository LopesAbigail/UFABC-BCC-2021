positivos = 0
negativos = 0
iguais_zero = 0

for i in range(0, 10):
    n = int(input())
    if (n > 0):
        positivos += 1
    elif (n < 0):
        negativos += 1
    else:
        iguais_zero += 1

print(positivos)
print(negativos)
print(iguais_zero)
