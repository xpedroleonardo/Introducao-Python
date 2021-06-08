# -*- coding: utf-8 -*-
soma = 0
total = 0

print("\nNÚMEROS INTEROS\n")

while 1:
  numero = int(input("Digite um número inteiro: "))

  if numero == 0:

    print(f"O Total de número digitados é: {total}")
    print(f"A soma dos números digitados é: {soma}")
    print(f"A média aritimética dos números digitados é: {soma / total}")

    break

  soma += numero
  total += 1