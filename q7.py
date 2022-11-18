''' Questão 7
O Crivo de Eratóstenes é uma técnica desenvolvida há mais de
2.000 anos para encontrar facilmente todos os números primos
entre 2 e algum limite. Segue-se uma descrição do algoritmo:
'''
#Crie um programa Python que use esse algoritmo para exibir todos 
# os números primos entre 2 e um limite inserido pelo usuário. 
# Se você implementar o algoritmo corretamente, deverá ser capaz de exibir 
# todos os números primos menores que 1.000.000 em alguns segundos.


from re import T

print()    
print('########### Teste de números Primos ############')
print()  
lista=list()
def funcao(r):
    for d in lista[:]:             
        if (((d % r) == 0) and (d != r)):
            lista.remove(d)

limite = int (input('Digite  o limite desejado:  '))

for a in range (2, limite):
    lista.append(a)
    
tamanho = len(lista)
for r in lista:
    funcao(r)
     
print (lista)
print('\n')
print('########### Fim de Teste ############')
print()