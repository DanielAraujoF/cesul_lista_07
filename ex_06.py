# 6) Desenvolva um programa que receba um número inteiro como entrada do usuário e verifique se o número informado é um
#    número primo. Um número primo é um número que somente pode ser divisível por 1 e por si mesmo.

numeroInf = int(input("Digite um número e o verificaremos se este é um número primo: "))

if ((numeroInf % 2 != 0) and (numeroInf % 3 != 0)) or numeroInf == 2:
    print("É um número primo.")
else:
    print("Não é um número primo.")
