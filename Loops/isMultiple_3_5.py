# Leia 8 numeros inteiros
# Imprima cada numero lido, seguido de (e de acordo com o caso):
# • " é múltiplo de três"
# • " é múltiplo de cinco"
# • " é múltiplo de três e cinco"
# Se não, imprima apenas o numero

def isMultiple_3_5(number):
    return_value = str(number)
    if (number % 3 == 0):
      if (number % 5 == 0):
          return_value += " é múltiplo de três e cinco"
      else:
          return_value += " é múltiplo de três"
    else:
      if (number % 5 == 0):
          return_value+" é múltiplo de cinco"
    return return_value

def isMultiple_3_5_test():
    if (isMultiple_3_5(451) == "451"):
        print("Com 451 funciou!")
    else:
        print("Com 451 não funciou!")
    if(isMultiple_3_5(1005) == "1005 é múltiplo de três e cinco"):
        print("Com 1005 funciou!")
    else:
        print("Com 1005 não funciou!")
    if(isMultiple_3_5(1465) == "1465 é múltiplo de cinco"):
        print("Com 1465 funciou!")
    else:
        print("Com 1465 não funciou!")
    if(isMultiple_3_5(2871) == "2871 é múltiplo de três"):
        print("Com 2871 funciou!")
    else:
        print("Com 2871 não funciou!")
    if(isMultiple_3_5(56) == "56"):
        print("Com 56 funciou!")
    else:
        print("Com 56 não funciou!")
    if(isMultiple_3_5(1385) == "1385 é múltiplo de cinco"):
        print("Com 1385 funciou!")
    else:
        print("Com 1385 não funciou!")
    if(isMultiple_3_5(54) == "54 é múltiplo de três"):
        print("Com 54 funciou!")
    else:
        print("Com 54 não funciou!")
    if(isMultiple_3_5(2028) == "2028 é múltiplo de três"):
        print("Com 2028 funciou!")
    else:
        print("Com 2028 não funciou!")


# With loop - without function
# for i in range(0,8):
    # numero = int(input())
    # if (numero % 15 == 0):
    #     print(numero, "é múltiplo de três e cinco")
    # else:
    #     if (numero % 5 == 0):
    #         print(numero, "é múltiplo de cinco")
    #     else:
    #         if(numero % 3 == 0):
    #             print(numero, "é múltiplo de três")
    #         else:
    #             print(numero)
