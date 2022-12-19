"""Exercicio 008
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

valor_hora = int(input('Quanto você ganha por hora? '))
qtd_horas = int(input('Quantas horas vc trabalhou nesse mês? '))
salario = qtd_horas * valor_hora

print(f'Seu salário esse mês foi R$:{salario}')
