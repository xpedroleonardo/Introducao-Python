# -*- coding: utf-8 -*-

print("TESTE DE MULTIPLA ESCOLHAS")
print("Seleciona a opção correta: a, b, c, d ou e\n")
corretas = 0

print("1 - Quanto é 1 + 1:\na) 1\nb) 2\nc) 3\nd) 4\ne) 5")
primeira = input("Digite a opção: ").lower()

if primeira == 'b':
  corretas+= 1

print("\n------------------\n")

print("2 - Quanto é 15 x 17:\na) 255\nb) 250\nc) 170\nd) 440\ne) 333")
segunda = input("Digite a opção: ").lower()

if segunda == 'a':
  corretas+= 1

print("\n------------------\n")

print("3 - Quanto é 10 em binário:\na) 1000\nb) 1100\nc) 0011\nd) 1010\ne) 0001")
terceira = input("Digite a opção: ").lower()

if terceira == 'd':
  corretas+= 1


if corretas == 3:
  print("Parabéns, você acertou todas as perguntas")
elif corretas == 2:
  print("Você acertou duas perguntas")
elif corretas == 1:
  print("Você acertou uma pergunta")
else:
  print("Infelizmente você não acertou nenhuma pergunta")