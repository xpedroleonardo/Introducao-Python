# -*- coding: utf-8 -*-

print("\nTABUADA\n")

numero = int(input("Digite um número: "))

print("\nAgora, selecione onde a tabuada começa e termina:")
comeca = int(input("Onde começa: "))
termina = int(input("Onde termina: "))

print(f"\nTabuada do {numero}, do {comeca} até {termina}: \n")

while comeca <= termina:
  print(f"{comeca} x {numero} = {comeca * numero}")
  comeca += 1

print("\nFim da tabuada\n")