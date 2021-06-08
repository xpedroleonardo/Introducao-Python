# -*- coding: utf-8 -*-

print("EMPRÉSTIMO BANCÁRIO\n")

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = float(input("Digite os anos para pagar: "))

porcentagemSalario = (30/100) * salario
meses = anos * 12
prestacao = round(casa / meses,2) 

if prestacao > porcentagemSalario:
  print("Empréstimo recusado!!!")
else:
  print("Empréstimo Aprovado!!! \nSua prestação mensal será de: R$", prestacao)
