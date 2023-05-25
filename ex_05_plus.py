# 5) Desenvolva um programa que sorteie um número entre 1 e 100 e dê ao usuário 10 chances de acertar o
# número sorteado. Se o usuário acertar, exibir o número de tentativas necessárias para o acerto. Se não
# acertar após as 10 tentativas, exibir o número sorteado.

import random

acertou = False

sorteio = random.randint(0, 10)

for i in range(1, 11):
    palpite = int(input("Insira o seu chute: "))

    if palpite == sorteio:
        print(f"Acertou em {i} tentativas! Meus parabéns!")
        acertou = True
        break
    else:
        print("Errou! Tente novamente.")
        if palpite < sorteio:
            print("Muito baixo!")
        elif palpite > sorteio:
            print("Muito alto!")

if not acertou:
    print(f"O número sorteado era {sorteio}.")

print("FIM.")
