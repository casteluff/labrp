n = int(input())

count = 1
while (n > 0):

    senhaFinal = []
    senhas = []
    linhas = []
    for e in range(n):
        linha = list(input().split())
        linhas.append(linha)
    for linha in linhas:
        for e in range(10):
            linha[e] = int(linha[e])

    
    for linha in linhas:
        senha = []
        for e in range(10, 16):
            if (linha[e] ==  'A'):
                senha.append(linha[0])
                senha.append(linha[1])
            elif (linha[e] ==  'B'):
                senha.append(linha[2])
                senha.append(linha[3])
            elif (linha[e] ==  'C'):
                senha.append(linha[4])
                senha.append(linha[5])
            elif (linha[e] ==  'D'):
                senha.append(linha[6])
                senha.append(linha[7])
            elif (linha[e] ==  'E'):
                senha.append(linha[8])
                senha.append(linha[9])
        senhas.append(senha)

    for e in range(0, 12, 2):
        nums = []
        for senha in senhas:
            nums.append(senha[e])
            nums.append(senha[e + 1])
        for num in nums:
            if (nums.count(num) == len(senhas)):
                senhaFinal.append(num)
                break

    
    print("Teste %d" % count)
    for d in senhaFinal:
        print(d, end="")
        print(" ", end="")
    print()
    print()
   

    n = int(input())
    count += 1