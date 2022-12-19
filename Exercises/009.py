"""Exercicio 009
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)."""

temp_f = int(input('Digite a temperatura em graus Fahrenheit: '))
temp_c = 5 * ((temp_f - 32) / 9)
print(f'A temperatura {temp_f}Fº em graus Celcius é {temp_c}Cº')