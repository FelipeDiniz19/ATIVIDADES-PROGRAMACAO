a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))

if a >= b and a >= c:
    print(f"maior{a}")

elif b >= a and b >= c:
    print(f"maior{b}")

else:
    print(f"maior {c}")


if a <= b and a <= c:
    print(f"menor{a}")

elif b <= a and b <= c:
    print(f"menor{b}")

else:
    print(f"menor{c}")

    
