# 8. Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento de um mês.
deposito = float(input('Digite o valor a ser depositado: R$'))
juros = float(input('Digite o percentual de juros para o rendimento: '))
rendimento = deposito * juros / 100
rendimento_total = deposito + rendimento
print('O rendimento foi de: R$',rendimento)
print('O valor total de saldo é de: R$', rendimento_total)