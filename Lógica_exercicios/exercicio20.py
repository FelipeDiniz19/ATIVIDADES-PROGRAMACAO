a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a >= b >= c:
    print(f"A ordem crescente: {c}, {b}, {a}")

elif b >= a >= c:
    print(f"A ordem crescente: {c}, {a}, {b}")

elif c >= a >= b:
    print(f"A ordem crescente: {b}, {a}, {c}")

elif c >= b >= a:
    print(f"A ordem crescente: {a}, {b}, {c}")

elif b >= c >= a:
    print(f"A ordem crescente: {a}, {c}, {b}")

else:
    print(f"A ordem crescente: {b}, {c}, {a}")

