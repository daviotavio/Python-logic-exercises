"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto.
quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$"""

valor_hora = int(input('Quanto você ganha por hora? '))
qtd_horas = int(input('Quantas horas vc trabalhou nesse mês? '))
salario_bruto = qtd_horas * valor_hora

ir =  (11/100) *salario_bruto
inss =  (8/100) * salario_bruto
sindicato = (5/100) * salario_bruto
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f'Seu salário bruto foi: {salario_bruto:,.2f}\n'
      f'E o seu salario liquido foi {salario_liquido:,.2f}'
)

