# 4) Desenvolva um programa que solicite ao usuário 10 números. Como resultado, apresentar o maior e o
# menor número informado.

maior = 0
menor = 0
for i in range(10):
    numero = int(input("Informe um número inteiro: "))

    if i == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f"O menor número é {menor} e o maior número é {maior}.")
