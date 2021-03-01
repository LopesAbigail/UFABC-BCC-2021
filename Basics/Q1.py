# O sistema deve
# 1. Receber coordenadas (x,y) do viajante
# 2. Receber a eficiência do carro do viajante (em Km/L)
# 3. Receber a quantidade de litros de combustível no carro do viajante
# 4. Calcular a distância a ser percorrida pelo carro - usar distância de pontos -> sqrt(x^2+y^2) -> math.sqrt(x**2 + y**2)
# 5. Ver quanto de combustível o carro usará para percorrer essa distância, de acordo com sua eficiência
#   efficiency = km/L => efficiency*litros é o quanto o carro consegue percorrer
# 6. Verificar se a quantidade de Km que o carro consegue percorrer é maior ou igual à distância
# 7. Se for maior ou igual, retornar "S"
# 8. Senão retornar "N"

import math

x = float(input())
y = float(input())
efficiency = float(input())
liter = float(input())

if (efficiency*liter >= math.sqrt(x**2 + y**2)):
    print("S")
else:
    print("N")
