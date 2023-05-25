# 5) Desenvolva um programa que sorteie um número entre 1 e 100 e dê ao usuário 10 chances de acertar o
# número sorteado. Se o usuário acertar, exibir o número de tentativas necessárias para o acerto. Se não
# acertar após as 10 tentativas, exibir o número sorteado.

import random
x = 11

numeroAleatorio = random.randint(0, 10)

print("\nFoi gerado um número aleatório entre 0 a 10, tente acertá-lo.")

for i in range(x):
    chute = int(input("Insira o seu chute: "))

    if chute != numeroAleatorio:
        print("Errou! Tente novamente.")

    else:
        print("Acertou! Meus parabéns!.")
        x = 1