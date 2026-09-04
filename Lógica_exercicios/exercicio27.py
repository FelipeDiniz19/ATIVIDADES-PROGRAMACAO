peso = float(input("Digite seu peso: "))
altura= float(input("Digite seu peso: "))


imc= peso / (altura * altura )

if imc <= 18.5 :
    print("ABAIXO DA FAIXA")

elif imc >= 18.5 and imc < 25:
    print("FAIXA NORMAL")

elif imc >= 25 and imc < 30:
    print("ACIMA DA FAIXA") 

else :
    print("FAIXA ELEVADA ")