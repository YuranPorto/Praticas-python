import random


def jogar():
    print('******************************************')
    print('***Bem	vindo	ao	jogo	da	Forca!***')
    print('******************************************')

    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in palavras:
        linha - linha.strip()
        palavras.append()
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    letras_acertadas = ['_' for letra in palavra_secreta]
    erros = 0
    acertou = False
    enforcou = False

    while not acertou and not enforcou:
        print(letras_acertadas)
        chute = str(input('Digite uma letra: ').lower())
        chute = chute.strip().lower()
        posicao = 1
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print(f'encontrei a letra {letra} na posição {posicao}')
                letras_acertadas[posicao - 1] = letra.upper()
            posicao += 1
        else:
            erros += 1
        acertou = '_' not in letras_acertadas
        enforcou = erros == len(letras_acertadas)

        if acertou:
            print('Parabéns, você acertou todas as letras')
            print('Fim de Jogo')
            print(letras_acertadas)
        elif enforcou:
            print('Você perdeu o jogo :/')
            print('Fim de Jogo')
