n = int(input())

trilhas = []
for e in range(n):
  trilha = list(map(int, input().split()))
  trilhas.append(trilha)

menor = 1000
indice = 0
comparadoresIda = []
for trilha in trilhas:
  altura = 0
  for valor in range(1, len(trilha) - 1):
    if (trilha[valor] < trilha[valor+1]):
      altura += trilha[valor+1] + trilha[valor]
  comparadoresIda.append(altura)

comparadoresVolta = []
for trilha in trilhas:
  altura = 0
  for valor in range(1, len(trilha) - 1):
    if (trilha[valor] > trilha[valor+1]):
      altura += trilha[valor+1] + trilha[valor]
  comparadoresVolta.append(altura)

for e in range(len(comparadoresIda)):
  if (comparadoresIda[e] < menor):
    menor = comparadoresIda[e]
    indice = e

for e in range(len(comparadoresVolta)):
  if (comparadoresVolta[e] < menor):
    menor = comparadoresVolta[e]
    indice = e

print (indice)