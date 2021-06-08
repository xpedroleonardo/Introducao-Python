def MatrizDigitada():
  LinhaQuantidade = int(input("Digite a quantidade de linhas da matriz: "))
  ColunaQuantidade = int(input("Digite a quantidade de colunas da matriz: "))

  return CriaMatrizDigitada(LinhaQuantidade, ColunaQuantidade)

def CriaMatrizDigitada(Linhas, Colunas):
  Matriz = []

  for L in range(Linhas):
    Linha = []

    for C in range(Colunas):
      Valor = int(input(f"Digite o Elemento [{str(L)}][{str(C)}]: "))
      Linha.append(Valor)

    Matriz.append(Linha)
  return ImprimeRaiz(Matriz)

def ImprimeRaiz(matriz):  
  print("\nMatriz: \n") 
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if (j == len(matriz[0])-1):
        print (matriz[i][j])
      else:
        print (matriz[i][j],end=' ')

MatrizDigitada()