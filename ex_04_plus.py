# 4) Desenvolva um programa que solicite ao usuário 10 números. Como resultado, apresentar o maior e o
# menor número informado.

import sys

maior = -sys.maxsize
menor = sys.maxsize
for i in range(10):
    numero = int(input("Informe um número inteiro: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"O menor número é {menor} e o maior número é {maior}.")
