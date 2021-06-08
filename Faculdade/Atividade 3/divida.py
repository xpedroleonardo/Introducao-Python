# -*- coding: utf-8 -*-

print("\nCALCULO DE DÍVIDA\n")

divida = float(input("Digite a sua dívida: "))
jurosMensal = float(input("Digite o juros mensal: "))
valor = float(input("Digite o valor mensal a ser pago: "))

totalJuros = 0
totalMeses = 0
totalPago = 0

while divida >= 0:
  juros = round((divida * jurosMensal) / 100, 2)
  totalJuros += round((divida * jurosMensal) / 100, 2)
  divida = round(divida + juros, 2)
  
  print("\n------------------------\n")

  print("juros ", juros)
  print("divida ", divida)

  divida = round(divida - valor, 2)

  print("divida pos ", divida)

  print("\n------------------------\n")

  totalPago += valor

  if divida <= 0:
    totalPago -= abs(divida)
  
  totalMeses += 1

print(f"Numero de Meses para a dívida ser paga: {totalMeses}")
print(f"O total pago é: R$ {totalPago}")
print(f"O total de juros é: R$ {round(totalJuros, 2)}")