# 6. Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.
salario = float(input('Digite o salário do funcionário: R$'))
gratificacao = salario * 5 / 100
imposto = salario * 7 / 100
salarioreceber = salario + gratificacao - imposto
print('O salário com gratificação e desconto de imposto é de: R$', salarioreceber)