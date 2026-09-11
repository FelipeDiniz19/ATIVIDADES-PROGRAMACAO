print("-----------------QUANTIDADES DE DIAS DO MES----------------")

mes = (int(input("Digite o numero do mes:  ")))

ano=int(input(" Digite um ano: "))

if mes in [1,3,5,7,8,10,12]:
    print("possui 31 dias")


elif mes in [4,6,9,11]:  
    print("possui 30 dias")

elif mes == 2 and (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
    print("POSSUI 29 DIAS.")

elif mes == 2:
    print("possui 28 dias")

else:
    print("MES INVALIDO")
