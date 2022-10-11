import random
def jogar():
    print('**********************************')
    print('*     Jogo da	adivinhação     *')
    print('**********************************')

    numero_secreto = random.randrange(1, 30)
    total_de_tentativas = 3

    while total_de_tentativas > 0:
        chute = int(input('Digite um número: '))
        print(f'Você digitou {chute}')

        if chute == numero_secreto:
            print('Parabéns, você acertou!!')
            break
        elif chute > numero_secreto:
            total_de_tentativas -= 1
            print('Você errou, seu chute foi maior que o número escolhido')
            print(f'Você ainda tem {total_de_tentativas} chances')
        elif chute < numero_secreto:
            total_de_tentativas -= 1
            print('Você errou, seu chute foi menor que o número escolhido')
            print(f'Você ainda tem {total_de_tentativas} chances')

    print('Fim de Jogo')
