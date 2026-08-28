n1 = float(input("Digite sua primeira nota: " ))
n2 = float(input("Digite sua segunda nota: " ))

media = (n1 +n2) / 2

if media >= 7:
    print(f"A media e: {media}")
    print("APROVADO")


elif media >=5 and media < 7 :
    print(f"A media e: {media}")
    print("RECUPERACAO")
    
else:
    print(f"A media e: {media}")
    print("REPROVADO ")
