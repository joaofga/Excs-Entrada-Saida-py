#16. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber, seguindo estas regras:

#a hora trabalhada vale a metade do salário mínimo.

#o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.

#o imposto equivale a 3% do salário bruto.

#o salário a receber equivale ao salário bruto menos o imposto.

horas = int(input('Digite quantas horas foram trabalhadas: '))
salariominimo = int(input('Digite o valor do salário mínimo: '))
valorhora = salariominimo / 2
salariobruto = valorhora * horas
imposto = salariobruto / 100 * 3
salarioliquido = salariobruto - imposto
print(f'O valor da hora trabalhada é de: R${valorhora:.2f}.')
print(f'O valor do salário sem descontos é de: R${salariobruto:.2f}.')
print(f'O valor pago de impostos é de: R${imposto:.2f}.')
print(f'O valor do salarioliquido é de: R${salarioliquido:.2f}.')