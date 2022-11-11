# vamos trabalhar com dados de textos usando varios metodos, para verificar e modificar o valor de uma variavel da clss str

from os import system 
system('cls')
nomecompleto = input('informe seu nome')

#tamanho da minha string
print('1. total de caracteres', len(nomecompleto))

#acessando um caracter a partir da posição

print ('2. o caracter da posição 2 é:',nomecompleto[2])

#transformando em maiuscula ou minuscula
print('3.texto em maisuculo',nomecompleto.upper())
print('3.texto em minusculo',nomecompleto.lower())
print('3.primeira letra mais',nomecompleto.capitalize())

#procurar a posição de um determinado caractere
print('6. posição do caracter espaço:', nomecompleto.find(' '))

# fatiar uma string ate uma detereminada posição
espaço =nomecompleto.find(' ')
print ('7. somente o primeiro nome', nomecompleto[0:espaço])






























