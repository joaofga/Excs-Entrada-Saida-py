#12. Faça um programa que receba dois números, calcule e mostre um elevado ao outro. #Use os caracteres **


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num1elev = num1 ** num2
num2elev = num2 ** num1
print('O resultado do 1º número elevado pelo 2º é: ', num1elev)
print('O resultado do 2º número elevado pelo 1º é: ', num2elev)
