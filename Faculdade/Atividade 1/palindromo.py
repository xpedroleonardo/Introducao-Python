# -*- coding: utf-8 -*-

print("PALÍNDROMO\n")
numero = int(input("Digite um número: "))

def reverseString(x):
  retorno = ''.join(reversed(x))
  return int(retorno)

if numero == reverseString(str(numero)):
  print("O número digitado é um Palíndromo")
else:
  print("O número digitado não é um Palíndromo")