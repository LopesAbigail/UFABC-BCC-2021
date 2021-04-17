i = 1
while(i < 5):
    numero = int(input())
    if numero > 141:
        print("Meta atingida")
        break
    else:
        print("Insuficiente")
        i -= 1
