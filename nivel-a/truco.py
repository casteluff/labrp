n = int(input())

pontosA = 0
pontosB = 0
ordem = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
for e in range(n):
    
    rodada = list(map(int, input().split()))
    a = 0
    b = 0

    for e in range(3):
        if (ordem.index(rodada[e]) >= ordem.index(rodada[e + 3])):
            a += 1
        else:
            b += 1
    
    if (a > b):
        pontosA += 1
    else:
        pontosB += 1

print("%d %d" % (pontosA, pontosB))