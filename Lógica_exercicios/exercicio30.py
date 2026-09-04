valor_imovel = float(input("Digite o valor do imovel: "))
salario = float(input("Digite o seu salario: "))
prazo = int(input("Digite o prazo: "))

prestacao = valor_imovel /(prazo*12)
limite = salario * 0.30

if prestacao <= limite :
    print(f"Limite: {limite}")
    print(f"prestacao: {prestacao}")
    print ("APROVADO")

else:
    print("REPROVADO")