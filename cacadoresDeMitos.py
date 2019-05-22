n = int(input())

resultado = 0
raios = []
for e in range(n):
    raio = list(map(int, input().split()))
    raios.append(raio)
    for f in range(0, len(raios) - 1):
        if (raio == raios[f]):
            resultado = 1
            break

print(resultado)
