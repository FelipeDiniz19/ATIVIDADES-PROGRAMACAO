#Exemplo 02 - Função

def calcular_media(lista_de_numeros):

 #essa função recebe uma lista de número, calculo e média e retorna o resultado

# a função 'Sum()' é uma função embutida do Python que soma 
# os itens de uma lista

total = sum(lista_de_numeros)

#função 'len()' é outra função embitida que retorna o número de itens da uma lista
quantidade = len(lista_de_numeros)

#Evita divisão por zero se a lista estiver vazio
if quantidade== 0:

media = total / quantidade
return media

#-----Como usar a função------

# Criamos uma lista de notas

notas_aluno1 = [8.5,7.0,9.0,10.0]

#Passamos a lista para o nossa função

media_aluno1 = calcular_media(nota_aluno)

print(f"A media do aluno 1 é: {mediia_aluno1}")


