# Lê quantas serão as colunas de pedras
n = int(input())

# Lê quantas pedras haverão em cada coluna e 
# armazena na lista "pedras". 
pedras = list(map(int, input().split()))

# Armazena o número total de pedras na variável "totalDePedras"
totalDePedras = 0
for pedra in pedras:
    totalDePedras += pedra

# Conta o número de pedras no topo
# e armazena na variável "topo"
# O número de pedras no topo é igual ao número de
# colunas somados. Exemplos:
# n = 1, topo = 1
# n = 3, topo = 3 + 2 + 1 = 5
# n = 5, topo = 5 + 4 + 3 + 2 + 1 = 15
topo = 0
for e in range(n + 1):
    topo += e

# Confere se a pilha de pedras pode formar
# uma escada perfeita e conta o número de
# de linhas de pedras adicionais (que não são necessárias
# para formar a escada). Pode formar escada perfeita se:
# totalDePedras = topo + n * e
empilhavel = False
adicional = 0
for e in range(100000):
    if (e > 0):           # If apenas para começar o laço do 1
        topo += n
        # Adiciona uma linha de pedras, se ao serem adicionadas
        # 999999 linhas o número ainda não bater com o totalDePedras,
        # então o conjunto não é empilhável 
    if (totalDePedras == topo):
        empilhavel = True          
        adicional = e # Adicional = número de linhas adicionais além do topo
        break

# Conta e imprime o número de movimentos necessários
# para que a escada seja formada
movimentos = 0
if (empilhavel):
    for e in range(1, len(pedras) + 1):
        # Confere se há pedras a mais em cada coluna
        if (pedras[e - 1] > (e + adicional)):
            # Adiciona o número de movimentos equivalente à
            # cada pedra a mais em cada coluna
            movimentos += pedras[e - 1] - (e + adicional)
    print (movimentos)

# Imprime a saída se a pilha de pedras
# não forem empilháveis
elif (not empilhavel):
    print(-1)


