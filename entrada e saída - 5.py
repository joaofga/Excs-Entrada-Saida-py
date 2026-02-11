# 5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
salario = float(input('Digite o salário do funcionário: '))
percentualaumento = int(input('Digite o percentual de aumento para o funcionário: '))
novosalario = salario + (salario * percentualaumento / 100)
print('O valor do salário reajustado é de: R$', novosalario)