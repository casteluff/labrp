n = int(input())

trilhas = []
for e in range(n):
  trilha = list(map(int, input().split()))
  trilhas.append(trilha)

alturas = []
for trilha in trilhas:
  altura = 0 
  alturaIda = 0
  alturaVolta = 0

  for num in range(1, len(trilha) - 1):
    valor = trilha[num]
    proximoValor = trilha[num + 1]
    if (valor < proximoValor):
      alturaIda += proximoValor - valor
    elif (valor > proximoValor):
      alturaVolta += valor - proximoValor
      
  if (alturaIda <= alturaVolta):
    altura = alturaIda
  elif (alturaIda > alturaVolta):
    altura = alturaVolta
  alturas.append(altura)

menor = 1001
indice = 0
for altura in range(len(alturas)):
  if (alturas[altura] < menor):
    menor = alturas[altura]
    indice = altura + 1

print(indice)