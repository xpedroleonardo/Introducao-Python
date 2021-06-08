import random

def main():
    MensagemAbertura()
    print("1 - Para criar um arquivo novo com palavras")
    opcao = int(input("2 - Para jogar \n"))

    if opcao == 1:
        print("\nVocê escolheu Criar um arquivo novo com palavras\n")
        arquivo = open('palavras.txt', 'w') # Criação do arquivo
        AcrescentaPalavras()
    elif opcao == 2:
        jogar()
    else:
        print("Ops, opção inválida! Comece novamente.")


def AcrescentaPalavras():
    palavraDigitada = input("\nDigite uma palavra (Enter para finalizar):")
    while len(palavraDigitada) > 0:
        arquivo = open('palavras.txt', 'a')
        palavraAdicionar = palavraDigitada + '\n'
        arquivo.write(palavraAdicionar)
        palavraDigitada = input("\nDigite uma palavra:")
    arquivo.close()


def jogar():
    palavra_secreta = CarregaPalavraSecreta()

    letras_acertadas = LetrasAcertadas(palavra_secreta)
    print (letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):
        chute = PedeChute()
        if(chute in palavra_secreta):
            MarcaChuteCorreto(chute, letras_acertadas, palavra_secreta)
            acertou = '_' not in letras_acertadas
            # Podemos ler o código acima como "'_' não está contido em letras_acertadas".        
            print(letras_acertadas)
        else:
            erros += 1
            print("Não tem a letra",chute)
        enforcou = erros == 6
    if(acertou):
        MensagemVencedor()
    else:
        MensagemPerdedor(palavra_secreta)
    print('Fim do jogo')


def MensagemAbertura():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')
    return


def CarregaPalavraSecreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()   
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def PedeChute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return chute
            
def LetrasAcertadas(palavra):
    return ['_' for letra in palavra]

def MarcaChuteCorreto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
        posicao += 1
    return

def MensagemVencedor():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::.  .'       ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    return

    
def MensagemPerdedor(palavra_secreta):
    print('Puxa, você foi enforcado!')
    print('A palavra era {}'.format(palavra_secreta))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|    XXXX    XXXX   | / ")
    print(" |    XXXX    XXXX   |/  ")
    print(" |    XXX      XXX   |   ")
    print(" |                   |   ")
    print(" \__       XXX     __/   ")
    print("   |\      XXX    /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")
    return

main()

