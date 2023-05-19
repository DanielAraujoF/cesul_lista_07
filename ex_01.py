# 1) Desenvolver um programa que receba como entrada um número inteiro, e exiba a tabuada
# deste número.

fix = int(input("Insira o número fixo: "))

for base in range(11):
    print(f"{fix} * {base} = {fix * base}")

print("-----")
for base in range(1, 11):
    print(f"{fix} * {base} = {fix * base}")