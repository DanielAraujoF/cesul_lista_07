# 6) Desenvolva um programa que receba um número inteiro como entrada do usuário e verifique se o número informado é um
#    número primo. Um número primo é um número que somente pode ser divisível por 1 e por si mesmo.

numeroInf = int(input("Digite um número e o verificaremos se este é um número primo: "))

# if ((numeroInf % 2 != 0) and (numeroInf % 3 != 0) and (numeroInf ** 1/2 == )) or numeroInf == 2:
#     print("É um número primo.")
# else:
#     print("Não é um número primo.")

import sys
x1 = sys.maxsize

x = numeroInf

for i in range(x1):
    y = x + 1
    x = y
    if numeroInf % x == 0:
        print("Não")
    else:
        print("É")
    break
