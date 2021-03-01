# O sistema deve
# 1. Receber a idade de uma pessoa
# 2. Verificar a idade dela conforme a validação:
# 3. Caso seja maior que 83, retornar "Fevereiro"
# 4. Caso seja maior que 73, retornar "Marco" 
# 5. Caso seja maior que 63, retornar "Abril"
# 6. Caso seja maior que 53, retornar "Maio"
# 7. Caso seja maior que 43, retornar "Junho"
# 8. Caso seja maior que 33, retornar "Julho"
# 9. Caso seja maior que 23, retornar "Agosto"
# 10. Caso seja maior que 13, retornar "Setembro"
# 11. Senão, retornar "Outubro"

age = int(input())

if age > 83:
    print("Fevereiro")
elif age > 73:
    print("Marco")
elif age > 63:
    print("Abril")
elif age > 53:
    print("Maio")
elif age > 43:
    print("Junho")
elif age > 33:
    print("Julho")
elif age > 23:
    print("Agosto")
elif age > 13:
    print("Setembro")
else:
    print("Outubro")
