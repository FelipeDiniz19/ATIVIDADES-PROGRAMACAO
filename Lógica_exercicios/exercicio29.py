a = int(input("Digite o numero de lados: "))
b = int(input("Digite o numero de lados: "))
c = int(input("Digite o numero de lados: "))

if a + b > c and  a + c > b and c + b > a :
    if a == b == c :
        print("EQUILATERO")
    
    elif a == b != c :
        print("ISOSCELES")

    elif a != + b != c :
        print("ESCALENO")


else:
    print("NAO FORMA TRIANGULO")