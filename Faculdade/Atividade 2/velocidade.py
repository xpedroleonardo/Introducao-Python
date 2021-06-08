# -*- coding: utf-8 -*-

print("\nRADAR\n")

velocidade = float(input("Digite a velocidade do seu carro (Km/h): "))

if velocidade > 80:
  print("\nVocê foi multado")
  valor = round((velocidade - 80) * 5, 2)

  print(f"O valor da sua multa é: R$ {valor}\n")