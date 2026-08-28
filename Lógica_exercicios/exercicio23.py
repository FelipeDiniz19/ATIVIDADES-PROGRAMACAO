idade = int(input("Digite sua idade: "))

if idade < 16 :
    print("Nao pode votar")

elif idade == 16 or idade < 17:
    print("Voto opcional")

elif idade >= 18 and idade <= 69 :
    print("Voto obrigatorio")

else:
    print ("Opcional")