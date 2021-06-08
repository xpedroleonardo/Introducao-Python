def CriaMatriz(Linhas, Colunas, Valor):
  matriz = []

  for i in range(Linhas):
    linha = []

    for j in range(Colunas):
      linha.append(Valor)

    matriz.append(linha)
  return matriz
