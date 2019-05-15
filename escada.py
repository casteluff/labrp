n = int(input())

pedras = list(map(int, input().split()))
totalDePedras = 0
for pedra in pedras:
    totalDePedras += pedra

num = 0
for e in range(n + 1):
    num += e

empilhavel = False
adicional = 0

for e in range(100000):
    if (e > 0):
        num += n
    if (totalDePedras == num):
        empilhavel = True
        adicional = e
        break

movimentos = 0
if (empilhavel):
    for e in range(1, len(pedras) + 1):
        if (pedras[e - 1] > e):
            if ((pedras[e - 1] - (e + adicional)) > 0):
                movimentos += pedras[e - 1] - (e + adicional)
    print (movimentos)

elif (not empilhavel):
    print(-1)