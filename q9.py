'''Questão 9
Crie um programa Python que leia um ou mais arquivos-fonte
Python e identifique funções que não são imediatamente
precedidas por um comentário. Para os fins deste exercício,
suponha que qualquer linha que comece com “def”, seguida por um
espaço, seja o início de uma definição de função. Suponha que o
caractere de comentário, “#”, será o primeiro caractere na linha
anterior quando a função tiver um comentário.'''

print()    
print('########### Inicio do Programa ############')
print() 

while True:
    try:
        Esc = input(str('Insira o arquivo que você deseja utilizar \n  arquivopy.txt ou arquivo2py.txt\n'))
        Arq = open(Esc, 'r')
        break
    except FileNotFoundError:
        print("Algo deu errado! Este arquivo não existe. por favor tente novamente...")

j = 0

for i in arq:
    j += 1
    if "def" in i:
        print(i, ' A função foi localizada com sucesso na linha: ', j)

arq.close()



print('\n')
print('########### Fim de Programa ############')
print()