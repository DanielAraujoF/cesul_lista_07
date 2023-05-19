# 2) Desenvolva um programa que receba um número inteiro como entrada do usuário e exiba
# todos os números de 0 até o número informado, substituindo aqueles divisíveis por 3 ou 7 pelo
# caractere “*”.

fim = int(input("Insira um número inteiro: "))

for i in range(0, fim + 1):
    if (i % 3 == 0) or (i % 7 == 0):
        print("*")
    else:
        print(i)
