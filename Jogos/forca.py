import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    erros = 0
    acertou = False
    enforcou = False
    palpites = []

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        elif chute in letras_acertadas:
            print(f'A letra {chute} já está na lista de acertos')
            print(letras_acertadas)
        elif chute in palpites:
            print(f'A letra {chute} já foi sugerida anteriormente')
        else:
            palpites.append(chute)
            print(palpites)
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_vencedor()
        print(letras_acertadas)
    elif enforcou:
        imprime_perdedor()


def imprime_mensagem_abertura():
    print('******************************************')
    print('***Bem	vindo	ao	jogo	da	Forca!***')
    print('******************************************')


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    print(palavra_secreta) # Para fins de teste
    return palavra_secreta


def inicializa_letras_acertadas(palavras):

    return ['_' for letra in palavras]


def pede_chute():
    chute = input('Chute uma letra: ')
    chute = chute.strip().lower()

    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_vencedor():
    print('Parabéns, você acertou todas as letras')
    print('Fim de Jogo')


def imprime_perdedor():
    print('Você perdeu o jogo :/')
    print('Fim de Jogo')

