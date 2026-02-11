# 7. Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que o funcionário tem gratificação de 50,00 sobre o salário base e paga imposto que deve ser lido e é aplicado sobre o salário base.
salario = float(input('Digite o salário aqui: R$'))
imposto = float(input('Digite o percentual de imposto sobre o salário base: '))
novosalario = salario + 50 - (salario * imposto / 100)
print('O salário com gratificação e descontodo de imposto é: R$', novosalario)
