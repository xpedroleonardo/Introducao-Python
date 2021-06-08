# import random

# arquivo = open('palavras.txt','w')
# arquivo.write('Banana\n')
# arquivo.write('Cebola\n')
# arquivo.write('Melancia\n')
# arquivo.close()

# -----------------------------

# arquivo = open('palavras.txt', 'r')
# linha = arquivo.readline()
# linha = linha.strip() # strip() -> Remove os caracteres especiais
# print(linha)

# -----------------------------

## Pegando as palavras do arquivo, e colocando no array

# arquivo = open('palavras.txt', 'r')
# palavras = []

# for linha in arquivo:
#   linha = linha.strip()
#   palavras.append(linha)

# arquivo.close() 

# posicao = random.randrange(0,len(palavras)) # Retorna uma posição aleatória, dentre as do array
# palavra = random.choice(palavras) # Retorna uma palavra aleatória, dentre as do array

# print(x)