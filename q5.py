'''
Escreva uma função que determina quantos dias há em um
determinado mês. Sua função terá dois parâmetros: o mês como
um número inteiro entre 1 e 12 e o ano como um número inteiro de
quatro dígitos. Certifique-se de que sua função informe o número
correto de dias em fevereiro para os anos bissextos. Utilizar a
função implementada no exercício 4.
'''
#Função
def variavel_ano(ano):
    
    if ((ano % 400 == 0) or (ano % 4 == 0)):
        resposta = ' Ano  Bissexto'
        return resposta
    if (ano % 100 == 0):
        resposta = ' Ano Não Bissexto'
        return resposta
    else:
        resposta = 'Ano Não Bissexto'
        return resposta

    #função dias de cada mês
def dias_mes(mes, ano):
    dias = 31
    if (mes == 2 and variavel_ano(ano) == 'Ano Bissexto'):
        dias = dias - 2
    if (mes == 2 and variavel_ano(ano) == 'Ano Bão Bissexto'):
        dias = dias - 3
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        dias = dias - 1
    return dias

print()    
print('########### Inicio do Programa ############')
print()
mes = int(input('\nDigite um numero  de um mês entre 1-12: '))
ano = int(input('Digite o ano com 4 digitos: '))
print('A quantidade de dias deste mês no ano de {} é de: {}'.format( ano ,dias_mes(mes, ano)))

print('\n')
print('########### Fim de Programa ############')
print()