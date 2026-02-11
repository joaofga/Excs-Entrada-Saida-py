# 10.1 Faça um programa que calcule e mostre a área de um círculo. Sabe-se que:
# O programa anterior também pode ser implementado
# usando este recurso/biblioteca math - matemática
import math
raio = float(input('Digite o raio do círculo que deseja calcular a área: '))
area = math.pi * math.pow(raio, 2)
print('A área do círculo calculado é de: ', area)