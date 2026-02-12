# 11. Faça um programa que receba um número, calcule e mostre:
# O número digitado ao quadrado
# O número digitado ao cubo
# A raiz do número digitado
# A raiz cúbica do número digitado

num1 = float(input('Digite um número: '))
quadrado = num1 ** 2
cubo = num1 ** 3
raiz = num1 ** (1/2)
raizcu = num1 ** (1/3)
print('O número digitado ao quadrado é: ', quadrado)
print('O número digitado ao cubo é: ', cubo)
print('A raiz quadrada do número digitado é: ', raiz)
print('A raiz cubica do número digitado é: ', raizcu)