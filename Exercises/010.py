"""Exercicio 010
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit."""

temp_c = int(input('Entre com o valor em graus Celcius: '))
temp_f = int((temp_c * 1.8) + 32)
print(f'A temperatura {temp_c}ºC em Fahrenheit é {temp_f}ºF')