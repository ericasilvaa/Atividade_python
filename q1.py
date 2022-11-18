'''
Questão 1
A padaria do Pão & Pão vende seus pães por R$ 4,60 cada. O
pão do dia anterior (pão dormido) tem um desconto de 60%.
Implemente um programa que leia o número de pães dormidos que
o usuário está comprando e exiba o preço normal do pão, o
desconto e o preço total. Todos os valores devem ser exibidos
usando duas casas decimais, e as casas decimais em todos os
números devem ser alinhadas.
'''

print()
qcomprada = int(input('Digite a quantidade de pão dormidos comprados: '))  #quantidade de pão

valnormal=(qcomprada*4.60)      #valor normal do pão
desconto=(valnormal * 0.4)      #valor do pão com desconto
totalpagar=valnormal-desconto   #valor total do pao

print()
print("########### Os valores são: ###########")
print("\nO Preço NORMAL do pão é R$:        {:.2f}".format(valnormal))
print("O Preço do pão com DESCONTO é R$:   {:.2f}".format(qcomprada,desconto))
print("O Preço TOTAL com os descontos é:   {:.2f}".format(qcomprada, totalpagar))
print()

print('########### Fim de Programa ############')
print()

