# -*- coding: utf-8 -*-

print("DISTÂNCIA DA VIAGEM \n")
distancia = float(input("Digite a distância que vai percorer (em Km): "))

if distancia <= 200:
  valorPassagem = distancia * 0.50
else:
  valorPassagem = distancia * 0.45

print("\nO valor da sua passagem é: R$", round(valorPassagem, 2), "\n")

print(f"Valor da Passagem: teste de variável {valorPassagem}")