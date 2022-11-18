''' Questão 6
Uma data mágica é uma data em que o dia multiplicado pelo mês
é igual ao ano de dois dígitos. Por exemplo, 10 de junho de 1960 é
uma data mágica porque junho é o sexto mês e 6 vezes 10 é 60, que
é igual ao ano de dois dígitos. Escreva uma função que determina
se uma data é ou não uma data mágica. Use sua função para criar
um programa principal que encontra e exibe todas as datas
mágicas do século XX. Utilize a função implementada no exercício
5.'''

print()    
print('########### Inicio do Programa ############')
print() 
#função verificação ano bissexto
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
    if (mes == 2 and variavel_ano(ano) == 'Ano bissexto'):
        dias = dias - 2
    if (mes == 2 and variavel_ano(ano) == 'Ano não bissexto'):
        dias = dias - 3
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        dias = dias - 1
    return dias

#função verificadora de data mágica
def magic (dia, mes, ano, etapa):
    if (etapa == 1):
        if (dia * mes == ano):
            return 'é uma data mágica'
        else:
            return 'Não é uma data mágica'

    if (etapa == 2):    
        if (dia * mes == ano):
            print ('{}/{}/{} é uma data Mágica'.format(dia, mes, ano))
        
    
#função que anlisa a data mágica
def identific_magic ():
    mes = 0
    ano = 0

    for a in range (1900,1999):
      ano = ano + 1
      mes = mes + 1
      if (mes > 12):
          mes = 1
      dias = dias_mes(mes, ano)
      for dia in range (1, dias):
         magic (dia, mes, ano, 2)
 
           
print('----Insira a DATA em formato XX/XX/XXXX----')
dia = int(input('\nInsira um dia do mês: '))
mes = int(input('\nInsira um mês:  '))
ano = int(input('\nInsiraum ano:  '))

print('\nA data escolhida: {}/{}/{}'.format(dia, mes, ano))
print ('A data escolhida : {}'.format(magic(dia, mes, ano, 1)))
print('\n')

print ('Principais datas mágicas referentes ao século XX são:')
identific_magic ()

print('\n')
print('########### Fim de Programa ############')
print()