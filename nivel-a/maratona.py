n, m = map(int, input().split())

consegue = True
distancias = list(map(int, input().split()))
distancias.append(42195)
for e in range(n):
    if (distancias[e + 1] - distancias[e] > m):
        consegue = False
        break

if (consegue):
    print('S')
else:
    print('N')