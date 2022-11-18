'''Uma roleta possui 38 espaços. Desses, 18 são pretos e 18 são vermelhos e 2 são verdes. Os espaços verdes são numerados 0 e
00. Os espaços vermelhos são numerados 1, 3, 5, 7, 9, 12, 14, 16,18, 19, 21, 23, 25, 27, 30 32, 34 e 36. Os números inteiros
restantes entre 1 e 36 são utilizados para numerar os espaços pretos.
Muitas apostas podem ser feitas na roleta. Vamos considerar apenas o seguinte subconjunto:
* Número único (1 a 36, 0 ou 00)
* Vermelho x Preto
* Ímpar contra par (0 e 00 não são considerados)
* 1 a 18 contra 19 a 36
'''
###Escreva um programa que simule o giro da roleta usando o método
###aleatório do Python de gerador de números. Mostre o número que
###foi selecionado e todas as apostas que devem ser pagas.

import random
print()
input("Pressione ENTER para girar a roleta\n")
print()
sorteio = random.randint(0,38)

if (sorteio % 2 == 0):
    classficacao = 'Par'
else: 
    classficacao = 'Ímpar'


if ((sorteio < 11) and (sorteio % 2 == 0)):
    cor =  'Preto'
if ((sorteio > 10 and sorteio < 20) and (sorteio % 2 != 0)):
    cor =  'Preto'
if ((sorteio > 19 and sorteio < 29) and (sorteio % 2 == 0)):
    cor =  'Preto' 
if ((sorteio > 28 and sorteio < 35) and (sorteio % 2 != 0)):
    cor =  'Preto'
else:
    cor =  'Vermelho'

if (sorteio == 0):
    cor = 'Verde' 

if (sorteio < 19):
    pague = '1 a 18'
else:
    pague = '19 a 36'

print()
print("########### RESULTADOS ###########")
print('\nO número sorteado é:    {}'.format(sorteio))
print('Cor:\t\t\t{}'.format(cor))
print('Classficação:\t\t{}'.format(classficacao))
print('Pagar:\t\t\t{}'.format(pague))
print()
print('######## Fim de Programa #########')
print()

