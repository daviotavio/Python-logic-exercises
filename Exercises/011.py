""" Exercicio 011
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo. """

print('Insira dois números inteiros e um real respectivamente: ')
n1 = int(input('Número inteiro 1 '))
n2 = int(input('Número inteiro 2 '))
n3 = float(input('Número real '))

produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
potencia = n3 ** 3
texto_potencia = f'{potencia:_.2f}'
texto_potencia = texto_potencia.replace('.', ',').replace('_', '.')

print(
    f'O produto do dobro do primeiro com metade do segundo é: {produto}\n'
    f'a soma do triplo do primeiro com o terceiro é: {soma}\n'
    f'o terceiro elevado ao cubo é igual a: {texto_potencia}'
)
