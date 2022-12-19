"""Exercicio 004
Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

n1 = float(input('Qual foi a sua nota do primeiro bimestre? '))
n2 = float(input('e do segundo bimestre?'))
n3 = float(input('e do terceiro bimestre?'))
n4 = float(input('e do quarto bimestre?'))
media = (n1 + n2 + n3 + n4) / 4

print(f'Sua média final foi {media}')
