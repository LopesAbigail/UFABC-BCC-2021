# O sistema deve:
# 1. Receber a área do cômodo
# 2. Verificar em qual condição ela se enquadra (tabela)
# 3. De acordo com a condição, imprimir uma recomendação:
# 4. Area < 11.2 -> Recomendamos 9000 BTU/h
# 5. 11.2 ≤ Area < 16.2 -> Recomendamos 12000 BTU/h
# 6. 16.2 ≤ Area < 21.2 -> Recomendamos 15000 BTU/h
# 7. 21.2 ≤ Area < 26.2 -> Recomendamos 18000 BTU/h
# 8. 26.2 ≤ Area ≤ 31.2 -> Recomendamos 21000 BTU/h
# 9. Senão -> Sem recomendacao

area = float(input())

if area < 11.2:
    print("Recomendamos 9000 BTU/h")
else:
    if 11.2 == area or area < 16.2:
        print("Recomendamos 12000 BTU/h")
    else:
        if 16.2 == area or area < 21.2:
            print("Recomendamos 15000 BTU/h")
        else:
            if 21.2 == area or area < 26.2:
                print("Recomendamos 18000 BTU/h")
            else:
                if 26.2 == area or area <= 31.2:
                    print("Recomendamos 21000 BTU/h")
                else:
                    print("Sem recomendacao")
