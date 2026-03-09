#14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
#a idade atual da pessoa;
#quantos anos ela terá em 2050.

dianascimento = int(input('Digite o seu dia de nascimento: '))
mesnascimento = int(input('Digite o mês do seu nascimento: '))
anonascimento = int(input('Digite o ano do seu nascimento: '))
diafuturo = int(input('Digite o dia no futuro para saber sua idade: '))
mesfuturo = int(input('Digite o mês no futuro para saber sua idade: '))
anofuturo = int(input('Digite o ano no futuro para saber sia idade: '))
diaatual = diafuturo - dianascimento
mesatual = mesfuturo - mesnascimento
anoatual = anofuturo - anonascimento
print(f'Na data digitada acima você terá {anoatual} anos, {mesatual} meses, {diaatual} dias!')