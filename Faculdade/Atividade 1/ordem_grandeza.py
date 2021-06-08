# -*- coding: utf-8 -*-

print("ORDEM DE GRANDEZA\n")

X = float(input("Digite um número: "))

if X > 0 and X < 100:
  print("\nO número digitado está entre 0 e 100\n")
elif X >= 100 and X < 1000:
  print("\nO número digitado está entre 100 e 1000\n")
elif X >= 1000 :
  print("\nO número digitado é maior ou igual a 1000\n")
else:
  print("\nO número digitado é  menor que zero\n")
