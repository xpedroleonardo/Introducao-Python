## CÓDIGO UTILIZADO PARA O PYTHON ENTENDER OS CARACTERES ESPECIAIS
## O CÓDIGO DEVE FICAR COMENTADO PARA FUNCIONAR
# -*- coding: utf-8 -*-

## VARIÁVEIS UTILIZANDAS

x = 1
y = 2
a = [1,2,3,4,5,6]
text = "Olá Mundo "

## EXIBE UMA MENSAGEM NA TELA: print()

# print(text)

## OPERADORES LÓGICOS: and | or | not

## ESTRUTURA CONDICIONAL

## IF

# if y > x:
#   print("y é maior")

## IF ELSE

# if x > y:
#   print("x é maior")
# else:
#   print("y é maior")

## IF ELIF

# if x > y:
#   print("x é maior")
# elif y > x:
#   print("y é maior")
# else:
#   print("x e y tem os mesmos valores")

## ESTRUTURA DE REPETIÇÃO

## WHILE

# while x <= 10:
#   print(x)
#   x += 1

## FOR

# for i in a:
#   print(i)

## FOR RANGE

# for i in range(10):
#   print(i)

## STRINGS

## TAMANHO DA STRING: len()

# print(len(text))

## INDICE DA STRING

# print(text[2])

## INDICE DA STRING ATÉ DETERMINADA POSIÇÃO

# print(text[0:3])

## TRANFORMAR TODAS AS LETRAS MINÚSCULAS: .lower()

# print(text.lower())

## TRANFORMAR TODAS AS LETRAS MAIÚSCULAS: .upper()

# print(text.upper())

## REMOVE CARACTERES ESPECIAIS DO FINAL DA STRING: .strip()

# print(text.strip())

## CONVERTE A STRING EM UM ARRAY: .split()

# print(text.split())

## BUSCANDO UM TRECHO DA STRING: Retorna a posição que a palavra começa

# print(text.find("Mundo"))

## SUBSTITUIR UM VALOR DA STRING: .replace()

print(text.replace("Mundo","World"))