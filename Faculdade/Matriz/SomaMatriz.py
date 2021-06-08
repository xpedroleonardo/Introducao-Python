import exemplos

mA = [[1,2],[3,4]]
mB = [[10,20],[30,40]]

def SomaMatriz(A,B):
  num_lin = len(A)
  num_col = len(A[0])
  C = exemplos.CriaMatriz(num_lin,num_col, 0)
  for i in range(num_lin):
    for j in range(num_col):
      C[i][j] = A[i][j] + B[i][j]
  return C

print(SomaMatriz(mA, mB))