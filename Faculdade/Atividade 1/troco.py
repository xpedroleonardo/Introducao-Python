# -*- coding: utf-8 -*-

contador = 1

print("PROGRAMA TROCO\n")

while contador == 1:

  numero = float(input('Digite um valor (R$): '))

  if numero >= 0.01:

    # Notas
    cem = int(numero / 100)
    numero = round(numero - (cem*100),2)

    cinquenta = int(numero/50)
    numero = round(numero - (cinquenta*50),2)

    vinte = int(numero/20)
    numero = round(numero - (vinte*20),2)

    dez = int(numero/10)
    numero = round(numero - (dez*10),2)

    quatro = int(numero/4)
    numero = round(numero - (quatro*4),2)

    um = int(numero/1)
    numero = round(numero - (um*1),2)

    # Centavos
    cinquentaCent = int(numero/0.50)
    numero = round(numero - (cinquentaCent*0.50),2)

    dezCent = int(numero/0.10)
    numero = round(numero - (dezCent*0.10),2)

    cincoCent = int(numero/0.05)
    numero = round(numero - (cincoCent*0.05),2)

    doisCent = int(numero/0.02)
    numero = round(numero - (doisCent*0.02),2)

    umCent = int(numero/0.01)
    numero = round(numero - (umCent*0.01),2)

    QuantNotas = [cem,cinquenta,vinte,dez,quatro,um]
    QuantMoedas = [cinquentaCent,dezCent, cincoCent,doisCent, umCent]
    Notas = ["R$ 100,00","R$ 50,00","R$ 20,00","R$ 10,00","R$ 4,00","R$ 1,00"]
    Moedas = ["R$ 0,50","R$ 0,10","R$ 0,05", "R$ 0,02","R$ 0,01"]

    print("\nValores a receber: \n")

    for Nota,QuantNota in zip(Notas, QuantNotas):
      if QuantNota > 0:
        print(QuantNota,"Notas" if QuantNota > 1 else "Nota", "de", Nota)

    for Moeda,QuantMoeda in zip(Moedas, QuantMoedas):
      if QuantMoeda > 0:
        print(QuantMoeda,"Moedas" if QuantNota > 2 else "Moeda", "de", Moeda)

    print("\n-------------------------\n")

  else: 

    print("Erro, valor inválido, tente novamente")
    print("\n-------------------------\n")

  continuar = 0
  while continuar == 0:
    print("Deseja continuar ?\n1) Sim\n0) Não")
    contador = int(input("Digite a opção: "))

    if contador == 1 or contador == 0:
      continuar = 1
    else:
      print("\nErro, selecione uma das opções")
      print("-------------------------\n")

  print("\n-------------------------\n")