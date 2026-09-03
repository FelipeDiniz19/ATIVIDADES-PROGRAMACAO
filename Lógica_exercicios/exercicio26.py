salario_atual = float(input(" Digite seu salario atual: "))

if  salario_atual <= 1500:
    novo_salario = salario_atual + (salario_atual*0.15)
    print(f"Seu salario com reajuste e de {novo_salario}")

elif 1500.01 <= salario_atual >= 3000:
    novo_salario = salario_atual + (salario_atual*0.10)
    print(f"Seu salario com reajuste e de {novo_salario}")

else:
    novo_salario = salario_atual + (salario_atual*0.05)
    print(f"Seu salario com reajuste e de {novo_salario}")

