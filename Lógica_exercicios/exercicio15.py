preco_unitario = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade: "))
frete = float(input("Digite o valor do frete: "))

subtotal = preco_unitario * quantidade

total = subtotal + frete

print (f"O subtotal e: {subtotal}")
print(f"O valor total e :{total}")



# Numeros utilizados para tesete :
# 10, 2, 10 ; 15,6,12; 13,2,4 