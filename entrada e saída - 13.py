#13. Sabe-se que:
#pé = 12 polegadas
#1 jarda = 3 pés
#1 milha = 1760 jarda
#Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre #os resultados.
#Polegadas;
#Jardas;
#Milhas.
pes = int(input('Digite a distância em pés: '))
polegadas = pes * 12
jarda = pes / 3
milha = jarda / 1760
print(f'A medida digitada em polegadas é: {polegadas:.2f}')
print(f'A medida digitada em jardas é: {jarda:.2f}')
print(f'A medida digitada em milhas é: {milha:.2f}')
