#15. O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:

#o valor correspondente ao lucro do distribuidor;

#o valor correspondente aos impostos;

#o preço final do veículo.

fabrica = float(input('Digite o preço de fábrica do veículo: '))
pimposto = float(input('Digite a % de juros do veículo: '))
plucro = float(input('Digite o % de lucro do distribuidor: '))
custofinal = fabrica + ((fabrica / 100) * pimposto) + ((fabrica / 100) * plucro)
valorimposto = (fabrica / 100) * pimposto
valorlucro = (fabrica / 100) * plucro
print(f'O valor final do veículo é de: R${custofinal:.2f}!')
print(f'O valor pago de impostos é de: R${valorimposto:.2f}!')
print(f'O lucro da distribuidora é de: R${valorlucro:.2f}!')