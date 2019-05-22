i, n = map(int, input().split())

jogadores = [['D'], ['E'], ['F']]
for e in range(3):
    jogadores[e].append(i)

for e in range(n):
    jogada = list(input().split())
    jogada[len(jogada) - 1] = int(jogada[len(jogada) - 1])

    if (jogada[0] == 'C'):
        for jogador in jogadores:
            if (jogador[0] == jogada[1]):
                jogador[1] -= jogada[2]
    elif (jogada[0] == 'V'):
        for jogador in jogadores:
            if (jogador[0] == jogada[1]):
                jogador[1] += jogada[2]
    elif (jogada[0] == 'A'):
        for jogador in jogadores:
            if (jogador[0] == jogada[1]):
                jogador[1] += jogada[3]
            elif (jogador[0] == jogada[2]):
                jogador[1] -= jogada[3]


for e in range(3):
    if (e == 2):
        print(jogadores[e][1])
    else:
        print(jogadores[e][1], end=" ")    


