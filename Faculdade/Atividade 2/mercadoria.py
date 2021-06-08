# -*- coding: utf-8 -*-

print("\nBem vindo a Loja\n")


produto = float(input("Digite o valor da mercadoria: "))
percentual = float(input("Digite percentual de desconto (%): "))

desconto = round((produto * percentual) / 100, 2)
valorfinal = round(produto - desconto, 2)


print(f"\n\nO desconto é de: R$ {desconto}")
print(f"O valor finar a pagar é: R$ {valorfinal}\n\n")
