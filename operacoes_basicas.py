a= int(input("coloque um numero :"))
b= int(input("coloque um numero :"))

soma = a + b            # Soma
subtracao = a- b        # Subtração
multiplicacao = a * b   # Multiplicação
divisao = a / b          # Divisão (sempre retorna um número com ponto flutuante, ex: float)
divisao_inteira = a // b   # Divisão inteira (descarta a parte decimal)
resto = a % b           # Resto da divisão (módulo)
potencia = a ** b        # Potência (a elevado a b)

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {potencia}")10
print("-" * 20)
