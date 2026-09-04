a = int(input("Digite o numero de lados: "))
b = int(input("Digite o numero de lados: "))
c = int(input("Digite o numero de lados: "))

if a + b > c and  a + c > b and c + b > a :
    print("Formam")

else:
    print("Nao formam")
