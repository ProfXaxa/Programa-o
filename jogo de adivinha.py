import random

# gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

max_tentativas = 5
tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")
# Loop do jogo
while tentativas < max_tentativas:
    # captura a entrada do usuário
        palpite = int(input("Digite seu palpite: "))

        tentativas += 1

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o numero em {tentativas} tentativas.")
            
        elif palpite < numero_secreto:
                print("Quase lá! Tente um número maior.")
        else:
                print("Quase lá! Tente um número menor.")

        if tentativas < max_tentativas:
                print(f"Você tem {max_tentativas - tentativas} tentativas restantes. ")
        else:
            print("Infelizmente, você não acertou. O número era", numero_secreto)
print("fim de jogo!")                