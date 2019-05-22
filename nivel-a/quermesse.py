n = int(input())

count = 1
while (n > 0):

    entry = list(map(int, input().split()))
    
    for e in range(n):
        if (entry[e] == e + 1):
            vencedor = entry[e]

    print("Teste %d" % count)
    print(vencedor)
    print()
    
    count += 1
    n = int(input())