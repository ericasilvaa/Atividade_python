'''A maioria dos anos tem 365 dias. No entanto, o tempo
necessário para a Terra orbitar o Sol é na verdade um pouco mais
do que isso. Como resultado, um dia extra, 29 de fevereiro, está
incluído em alguns anos para corrigir essa diferença. Esses anos
são chamados de anos bissextos.
As regras para determinar se um ano é ou não um ano bissexto são
as seguintes:
* Qualquer ano divisível por 400 é um ano bissexto.
* Dos anos restantes, qualquer ano divisível por 100 não é um ano
bissexto.
* Dos anos restantes, qualquer ano divisível por 4 é um ano
bissexto.
* Todos os outros anos não são anos bissextos.
Faça uma função que receba um ano e retorne se o ano é bissexto.'''

#Inicio do programa
print()
print('###########  Teste de Ano ########### ')
#Função
def variavel_ano(ano):

    if ((ano % 400==0) or (ano % 4 == 0)):
        resposta = ' é Bissexto'
        return resposta

    if (ano % 100 == 0):
        resposta = ' Não Bissexto'
        return resposta

    else:
        resposta = 'Não Bissexto'
        return resposta

ano = int (input('\nInforme um Ano: '))
    
print ('\nO ano de {}, {}'.format(ano,variavel_ano(ano)))
print()
print('########### Fim de Teste ############')
print()