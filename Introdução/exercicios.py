# -*- coding: utf-8 -*-

print("EXERCÍCIO 1")
print("Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.\n")

idade = int(input("Digite a sua idade: "))

if idade >= 18:
  print("\nVocê é maior de idade\n")
else:
  print("\nVocê é menor de idade\n")

########################################

print("EXERCÍCIO 2")
print("Faça um programa que receba duas notas digitadas pelo usuário.")
print("Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.\n")

primeiraNota = float(input("Digite a sua primeira nota: "))
segundaNota = float(input("Digite a sua segunda nota: "))

media = (primeiraNota + segundaNota) / 2

if media >= 6:
  print("\nParabéns, você passou!!!\n")
else:
  print("\nInfelizmente você reprovou\n")

######################################

print("EXERCÍCIO 3")
print("Escreva um programa que resolva uma equação de segundo grau.\n")

from math import sqrt

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - 4*a*c

try:
  raiz = sqrt(delta)
  x1 = (-b + raiz)/2*a
  x2 = (-b + raiz)/2*a

  print("\nAs raízes são", round(x1,2), "e", round(x2,2),"\n")
except:
  print("\nDelta negativo\n")

######################################

print("EXERCÍCIO 4")
print("Escreva um programa que ordene uma lista numérica com três elementos.\n")

lista = [3,1,2]
print("Lista: ",lista)
print("Lista ordenada: ",sorted(lista),"\n")

#####################################

print("EXERCÍCIO 5")
print("Escreva um programa que receba dois números e um sinal,")
print("e faça a operação matemática definida pelo sinal.\n")

primeiroNumero = int(input("Digite o primeiro número: "))
print("\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n")
operacao = input("Selecione a operação: ")
segundoNumero = int(input("\nDigite o segundo número: "))

if operacao == "1":
  print("\nResultado da adição:",primeiroNumero+segundoNumero)
elif operacao == "2":
  print("\nResultado da subtração:",primeiroNumero-segundoNumero)
elif operacao == "3":
  print("\nResultado da divisão:",primeiroNumero/segundoNumero)
elif operacao == "4":
  print("\nResultado da multiplicação:",primeiroNumero*segundoNumero)
else:
  print("\nErro, operação inválida")

print("\nEXERCÍCIOS FINALIZADOS")