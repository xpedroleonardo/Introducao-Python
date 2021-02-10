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

# print(text.replace("Mundo","World"))

## FUNÇÕES: def

# def soma(x, y):
#   print(x+y)

# soma(1,2)

## MANIPULAÇÃO DE ARQUIVOS

## ABRINDO ARQUIVOS: open(nome, modo)

# arquivo = open("./Introdução/arquivo.txt")

## LENDO AQUIVOS: .read(), .readline() e .readlines()

# textoArquivo = arquivo.read()
# print(textoArquivo)

# linhaArquivo = arquivo.readline()
# print(linhaArquivo)

# linhasArquivo = arquivo.readlines()
# print(linhasArquivo)

## CRIANDO AQUIVO: open("...","w"), .write() e .close()

# criando = open("./Introdução/criando.txt", "w")

# criando.write("Esse é o arquivo Criado!!!")

# criando.close()

## Listas (ARRAY)

## .append() : adiciona um valor no final

# a.append(7)
# print(a)

## VERIFICANDO ITENS NA LISTA

# if 1 in a:
#   print("Esse valor está na lista")

## REMOVENDO ITENS DA LISTA 

# del a[0:3] #posição que começa e termina de apagar
# print(a)

# del a[:] #apaga tudo da lista
# print(a)

## ORDENANDO A LISTA

# a.sort()  # Crescente, altenado a original
# print(a)

# a = sorted(a)  # Crescente, não altenado a original
# print(a)

# a.sort(reverse = True)  # Decrecente, altenado a original
# print(a)

# a.reverse() # Reverte a posição dos itens da lista
# print(a)


## DICIONÁRIOS (OBJETO)

# dados = {
#   "Nome": "Pedro Leonardo",
#   "GitHub": "xpedroleonardo",
#   "Repository": "Python"
# }

# print(dados["Nome"])  # Exibir um valor

# for d in dados.values(): # Exibir todos os valores
#   print(d) 

# for d in dados.items():  # Exibe a chave e o valor
#   print(d)

## NÚMEROS ALEATÓRIOS

# import random

# aleatorio = random.randint(0,10)
# print(aleatorio)

# numero = random.choice(a)  #Escolhe um dos valores da lista
# print(numero)

## TRATAMENTO DE EXECEÇÕES

try:
  print(2/0)
except:
  print("Não é possível realizar a divisão com 0")