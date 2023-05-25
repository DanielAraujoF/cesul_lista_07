# 6) Desenvolva um programa que receba um número inteiro como entrada do usuário e verifique se o número informado é um
#    número primo. Um número primo é um número que somente pode ser divisível por 1 e por si mesmo.

numeroInf = int(input("Digite um número e o verificaremos se este é um número primo: "))

primo = True
for i in range(2, numeroInf):
    if numeroInf % i == 0:
        primo = False
        break

if not primo:
    print("Não é primo!")
else:
    print("É primo!")
