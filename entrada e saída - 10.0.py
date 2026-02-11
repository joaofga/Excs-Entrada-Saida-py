# 10. Faça um programa que calcule e mostre a área de um círculo. Sabe-se que:
# area = pi * raio²
# Como pi é um valor que conhecemos, então use a seguinte fórmula:
# area = 3.1415 * raio²
raio = float(input('Digite o raio do círculo que deseja calcular a área: '))
area = 3.1415 * (raio * raio)
print('A área do círculo calculado é de: ', area)
