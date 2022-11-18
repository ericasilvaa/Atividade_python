''' Questão 10
A distância entre duas strings é uma medida de sua
similaridade - quanto menor a distância, mais semelhantes as
strings são em relação ao número mínimo de operações de
inserção, exclusão e substituição necessárias para transformar uma
string na outra.
Escreva uma função recursiva que calcule a distância de edição
entre duas strings.'''
###Use sua função recursiva para escrever um programa que lê duas strings do usuário e 
# exibe a distância de edição entre elas.

print()    
print('########### Inicio do Programa ############')
print() 

#Função recursiva
def D_Recursiva(s,t):

  if (len(s)==0):
    return len(t)

  elif(len(t)==0):
    return len(s)

  else:
    custo = 0

  if(s[-1:]!=t[-1:]):
     custo = 1

  res  =  min ([D_Recursiva( s [: - 1 ],  t ) + 1 ,
               D_Recursiva( s ,  t [: - 1 ]) + 1 ,
               D_Recursiva( s [: - 1 ],  t [: - 1 ])  +  custo ])

  return res

s = input('Insira a 1 palavra : ')
t = input('Insira a 2 palavra : ')
print('A distância entre as palavras é igual à:',D_Recursiva(s,t))


print('\n')
print('########### Fim de Programa ############')
print()