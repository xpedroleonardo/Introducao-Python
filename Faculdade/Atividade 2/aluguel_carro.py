# -*- coding: utf-8 -*-

print("\nALUGUEL DE CARROS\n")

print("Digite as informações do carro alugado")
percorrido = float(input("Digite a distância (KM) percorridos: "))
dias = int(input("Digite por quantos dias alugou: "))


total = (round(percorrido * 0.15,2)) + (dias * 60)

print(f"\nO preço a pagar é: R$ {total}\n")