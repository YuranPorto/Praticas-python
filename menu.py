import adivinhacao, forca
print('************************************')
print('**********MENU	DE	JOGOS**********')
print('************************************')
print('\n')
print('Digite 1 para jogar jogo da adivinhação\nDigite 2 para jogo da forca')
escolha = int(input('Digite o jogo que deseja jogar: '))
if escolha == 1:
    adivinhacao.jogar()
elif escolha ==2:
    forca.jogar()
