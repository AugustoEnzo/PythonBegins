# Expressões algébricas:
# Escreva as seguintes expressões algébricas em linguagem Python:
# a) O somatório dos 5 primeiros números inteiros e positivos

n1 = int(input('Insira o 1ª número: '))
n2 = int(input('Insira o 2ª número: '))
n3 = int(input('Insira o 3ª número: '))
n4 = int(input('Insira o 4º número: '))
n5 = int(input('Insira o 5ª número: '))
calc = n1 + n2 + n3 + n4 + n5

print('O resultado da soma dos números: {}, {}, {}, {} e {} resulta em: {}' .format(n1, n2, n3, n4, n5, calc))

# b) a média entre 23, 19 e 31
media_calc = (23 + 19 + 31)/3
print('A média de 23, 19 e 31 seria: {}' .format(media_calc))

# c) O número de vezes que 73 cabe em 403
i = 0
c = 0

while i < 403:
    print(i)
    i += 73
    c += 1
    print(c)

print('O número de vezes que 73 cabe em 403 é igual a 403')

#d) A sobra quando 403 é dividido por 73:
calc = 403 % 73
print('O resto da divisão de 403 por 73 é igual a: {}' .format(calc))

# e) 2 elevado à 10ª potência:
calc = 2**10
print('2 elevado a 10ª potência resulta em {}' .format(calc))

# f) O valor absoluto da diferença entre 54 e 57
calc = abs(57 - 54)
print('O valor absoluto da diferença entre 57 e 54 seria de: {}'. format(calc))

# g) O menor valor entre 34, 29 e 31:
calc = min(34, 29, 31)
print('O menor valor dentre 34, 29 e 31 seria: {}' .format(calc))

# Atribuição:
# Escreva as expressões em Pyhton para:
# a) Atribuir o valor inteiro 3 à variável a
a = int(3)

# b) atribuir o valor 4 à variável b
b = 4

# c) Atribuir à variável c o valor da expressão a*a + b * b
c = a * a + b * b

# Strings
# Execute as seguintes atribuições:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Agora, utilizando os operadores + e *, crie as saídas a seguir:
print(s1 +' ' + s2 + ' '+ s3)
print((s1 + ' ') * 10)
print(s1 + ' ' + (s2 + ' ') * 2 + (s3 + ' ') * 3)
print((s1 + ' ' + s2 + ' ') *7 )
print((s2 + s2 + s3 + ' ') * 5)

# Exercício 1
# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto.
produto = str(input('Indique o nome do produto: '))
preco = float(input('Indique o preço do produto: '))
desconto = float(input('Indique o percentual de desconto do produto: '))
calc_desc = preco * desconto
calc_preco = preco - calc_desc
print('O valor do desconto do produto {} foi igual a {}, o valor do produto com desconto é de {}' .format(produto, calc_desc, calc_preco))

# Exercício 2
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custo R$60 por dia e R$0,15 por km rodado.
km_perc = float(input('Insira a quantidade de kilometros percorridos: '))
dia_alug = float(input('Insira a quantidade de dias alugados: '))

calc = (dia_alug * 60) + (km_perc * 0.15)
print('No total de seu contrato o carro custou: {}' .format(calc))

# Exercício 3
# Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string digitada. Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string

string1 = 'Frase qualquer, só que não'
len_st1 = int(len(string1) / 2)
string2 = string1[:len_st1]
len_st2m2 = len(string2) - 2
string3 = string2[len_st2m2:]
print('Os dois últimos caracteres da segunda variável são: {}' .format(string3))

