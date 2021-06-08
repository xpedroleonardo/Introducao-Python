# -*- coding: utf-8 -*-

print("\nENERGIA ELÉTRICA\n")

quant = float(input("Digite a quantidade de kWh consumida: "))
print("Qual é o seu tipo de instalação:\n")

print("R - residencial\nI - industrial\nC - comércios\n")
tipo = input("Selecione uma opção: ").upper()

def calc(preco):
  return round(quant * preco, 2)

if tipo == "R":

  if quant <= 500:
    valor = calc(0.40)
  else:
    valor =  calc(0.65)

elif tipo == "C":

  if quant <= 1000:
    valor =  calc(0.55)
  else:
    valor =  calc(0.60)

elif tipo == "I":

  if quant <= 5000:
    valor =  calc(0.55)
  else:
    valor =  calc(0.60) 

else:
  print("\nErro, selecione uma instalação válida")

print(f"\nO valor a pagar é: R${valor}")