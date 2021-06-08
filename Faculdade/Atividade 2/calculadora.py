# -*- coding: utf-8 -*-

print("\nCALCULADORA\n")

primeiro = float(input("Digite o primeiro número: "))
segundo = float(input("Digite o segundo número: "))

print("\nSoma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão (/)\n")

opc = input("Selecione uma operação: ")

if opc == "+":
  print("\nO resultado da operação (+) é: ", round(primeiro + segundo, 2))
elif opc == "-":
  print("\nO resultado da operação (-) é: ", round(primeiro - segundo, 2))
elif opc == "*":
  print("\nO resultado da operação (*) é: ", round(primeiro * segundo, 2))
elif opc == "/":
  print("\nO resultado da operação (/) é: ", round(primeiro / segundo, 2))
else:
  print("Erro, selecione umas das operações")