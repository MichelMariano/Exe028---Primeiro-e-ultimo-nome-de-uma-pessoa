# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# primeiro e ultimo nome separadamente.

# Exemplo:
# Nome: Ana Maria de Souza
# primeiro: Ana
# último: Souza


n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()
print('É um prazer em te conhecer {} '.format(n))
print('Seu primeiro nome é: {} '.format(nome[0]))
print('Seu último nome é: {} '.format(nome[len(nome)-1]))
