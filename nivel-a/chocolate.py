n = int(input())

divisoes = list(map(int, input().split()))

pedacos = 0
for e in range(n):
    pedacos += divisoes[e] - 1

print(pedacos)