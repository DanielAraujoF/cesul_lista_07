# 3) Desenvolva um programa que receba como entrada do usuário a população de uma cidade e a taxa de
# crescimento anual da população. Apresentar como resultado qual será a população da cidade em 15 anos.

# v1
# popAtual = int(input("Qual a população na atualidade da cidade? "))
populacao = int(input("Qual a população na atualidade da cidade? "))
taxaCresc = float(input("Qual a taxa de crescimento populacional dessa cidade? "))

tempo = 15

# v1
# for i in range(1, tempo + 1):
#     popAumento = popAtual * (taxaCresc / 100)
#     popFut = popAtual + popAumento
#     popAtual = popFut
for i in range(1, tempo + 1):
    populacao += int(populacao * (taxaCresc / 100))

print(f"No {tempo}° ano, a população será de {populacao:.0f}.")
