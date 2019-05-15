# Lê quantas serão as colunas de pedras
n = int(input())

# Lê quantas pedras haverão em cada coluna
pedras = list(map(int, input().split()))
totalDePedras = 0
for pedra in pedras:
    totalDePedras += pedra

# Conta o número de pedras no topo
# e armazena na variável "num""
num = 0
for e in range(n + 1):
    num += e

# Confere se a pilha de pedras pode formar
# uma escada perfeita e conta o número de
# de linhas de pedras adicionais (que não são necessárias
# para formar a escada)
empilhavel = False
adicional = 0
for e in range(100000):
    if (e > 0):
        num += n
    if (totalDePedras == num):
        empilhavel = True
        adicional = e
        break

# Conta e imprime o número de movimentos necessários
# para que a escada seja formada
movimentos = 0
if (empilhavel):
    for e in range(1, len(pedras) + 1):
        if (pedras[e - 1] > e):
            if ((pedras[e - 1] - (e + adicional)) > 0):
                movimentos += pedras[e - 1] - (e + adicional)
    print (movimentos)

# Imprime a saída se a pilha de pedras
# não forem empilháveis
elif (not empilhavel):
    print(-1)