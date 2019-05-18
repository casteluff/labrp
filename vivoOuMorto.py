entrada = list(map(int, input().split()))

contador = 1
while (entrada[0] > 0):
    
    fila = list(map(int, input().split()))
    for e in range(entrada[1]):
        rodada = list(map(int, input().split()))
        ordem = rodada[1]

        toDelete = []
        for f in range(rodada[0]):
            if (rodada[f + 2] != ordem):
                toDelete.append(f)
        
        toDelete.sort(reverse=True)
        for i in toDelete:
            del fila[i]
            
    
    print("Teste %d" % contador)
    print(fila[0])
    print()

    contador += 1
    entrada = list(map(int, input().split()))