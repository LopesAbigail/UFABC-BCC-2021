# O sistema deve
# 1. Receber nota p1 e nota p2
# 2. Receber a presença
# 3. Calcular a média simples entre p1 e p2
# 4. Se a média >= 50 e presença >= 75, imprimir "S"
# 5. Senão imprimir "N"

p1 = float(input())
p2 = float(input())
attendance = float(input())

if ((p1+p2)/2 >= 50.0) and (attendance >= 75):
    print("S")
else:
    print("N")
