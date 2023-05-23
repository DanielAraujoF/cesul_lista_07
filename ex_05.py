# 5) Desenvolva um programa que sorteie um número entre 1 e 100 e dê ao usuário 10 chances de acertar o
# número sorteado. Se o usuário acertar, exibir o número de tentativas necessárias para o acerto. Se não
# acertar após as 10 tentativas, exibir o número sorteado.

import random
numeroAleatorio = random.randrange(10)

numeroInformado = int(input("Foi gerado um número aleatório entre 0 a 10, tente acertá-lo.\n Informe um número: "))

if numeroInformado == numeroAleatorio:
    print("Acertou! Meus parabéns!")
else:
    print(f"Errou! O número aleatório era {numeroAleatorio}. Tente novamente.")