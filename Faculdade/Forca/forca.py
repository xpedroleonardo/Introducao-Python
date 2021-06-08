palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
print(letras_acertadas)

acertou = False
enforcou = False
erros = 0

while (not acertou and not enforcou):
  chute = input("Qual letra?")
  if(chute in palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
      if (chute.upper() == letra.upper()):
        print('Encontrei a letra {} na posição {}'.format(letra, posicao))
        letras_acertadas[posicao] = letra
      posicao += 1
  else:
    erros += 1

  acertou = '_' not in letras_acertadas
  enforcou = erros == 6

  print(letras_acertadas)

if(acertou):
  print('\nVocê ganhou!!\n')
else:
  print('\nVocê perdeu!!\n')

print('Fim do jogo')
