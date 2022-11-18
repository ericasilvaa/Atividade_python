'''Questão 8
No jogo Scrabble, cada letra possui uma pontuação. A pontuação
total da palavra é a soma da pontuação das letras. As letras mais
comuns valem menos pontos, as letras menos comuns valem mais
pontos.'''
#Escreva um programa que computa e apresenta a pontuação para uma palavra. 
# Crie um dicionário que mapeie as letras e valores. 
# Utilize o dicionário para computar a pontuação.

print()    
print('########### Programa de Letras ############')
print()  


dados = dict()
Scrabble = {
    'A':1,
    'E':1,
    'I':1,
    'L':1,
    'N':1,
    'O':1,
    'R':1,
    'S':1,
    'T':1,
    'U':1,
    'D':2,
    'G':2,
    'B':3,
    'C':3,
    'M':3,
    'P':3,
    'F':4,
    'H':4,
    'V':4,
    'W':4,
    'Y':4,
    'K':5,
    'J':8,
    'X':8,
    'Q':10,
    'Z':10}

pontuação = 0
palavras = (input("escreva qualquer palavra: ")).upper()

for i in Scrabble:
        for j in palavras:
            if i == j:
                pontuação += Scrabble[i]

print('o Valor da  palavra  é :',pontuação)

print()
print('########### Fim de Programa ############')
print()