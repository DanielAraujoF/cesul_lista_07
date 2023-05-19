# 4) Desenvolva um programa que solicite ao usuário 10 números. Como resultado, apresentar o maior e o
# menor número informado.

maior = 1
menor = 100
for i in range(10):
    numero = int(input("Digite um número de 0 a 100: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    else:
        print(i)

print(f"O menor número é {menor} e o maior número é {maior}.")