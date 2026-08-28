preco = float(input("Digite o valor:"))
opcao = int(input("Digite a opcao: "))

if opcao == 1 :
    valor = preco - (preco * 0.10)
    print(f"seu valor e: {valor}")

elif opcao == 2:
    valor = preco - (preco * 0.05)
    print(f"seu valor e: {valor}")

elif opcao == 3 :
    valor = preco
    print(f"seu valor e: {valor}")

else:
    valor = preco + (preco * 0.08)
    print(f"seu valor e: {valor}")

