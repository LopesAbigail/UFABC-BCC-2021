# Sejam:
# p a populacao de uma cidade
# txContagio a taxa de contagio por gripe nessa cidade
# ct(i) o numero de pessoas contaminadas em um dia i
# ct(0) = 1439
# ct(i) = Ct(i−1) ∗ txContagio (somente pessoas que foram infectadas no dia i−1 podem infectar pessoas no dia i)
# 0 < i ≤ numDiasImunidadeColetiva

# Qualquer pessoa ja contaminada vai sobreviver e ter imunidade pelo resto do tempo
# O calculo do numero de pessoas imunizadas na cidade e cumulativo (pessoas imunizadas no dia 5 = Ct0 + Ct1 + Ct2 + Ct3 + Ct4 + Ct5)
# A imunidade coletiva nessa populacao ocorrera quando o numero de contaminados for maior ou igual a 74.0% do total

# Ler um numero inteiro para p
# Ler um numero real para txContagio
# Verificar se o mesmo é maior que 1
# Se for, calcular em quantos dias a populacao tera imunidade coletiva
# Raciocínio:
#   enquanto o numero de pessoas imunizadas for menor do que 74% da populacao, as contaminacoes ainda ocorrem e o dia incrementa
#   numero de pessoas imunizadas = numero de pessoas imunizadas no dia anterior * taxa de contagio
# 0.74 * numero_populacao = (contaminacoes_dia_0 * (1 - taxa_contagio^dias_para_imunizacao_coletiva)) / (1 - taxa_contagio)
# 17 dias

# Retornar no formato: A cidade conseguiu imunidade coletiva em 17 dias
# Restricao: nao usar lista

numero_populacao = int(input())
taxa_contagio = float(input())
pessoas_contaminadas_dia_0 = 1439
pessoas_imunizadas = 1439
dias_para_imunizacao_coletiva = 0


while(pessoas_imunizadas < 0.74 * numero_populacao):
    pessoas_contaminadas_dia_0 = pessoas_contaminadas_dia_0 * taxa_contagio
    pessoas_imunizadas += pessoas_contaminadas_dia_0
    dias_para_imunizacao_coletiva += 1
print("A cidade conseguiu imunidade coletiva em %.f dias" %
      dias_para_imunizacao_coletiva)
