# -*- coding: utf-8 -*-

print("\nCALCULO TEMPO DE VIDA\n")

cigaros = int(input("Digite a quantidade de cigarros fumados (por dia): "))
anos = float(input("Digite quantos há quantos anos fuma: "))

minutos = 10 * (cigaros * (anos * 365))
dias = round(minutos / 1440, 2)

print(f"\nA quantidade de dias perdidos é: {dias}\n")