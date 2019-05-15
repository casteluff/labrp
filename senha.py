# Lê quantas senhas serão lidas
n = int(input())

# Enquanto houver caso de teste resolva o caso de teste atual
# Contador para imprimir o número na saída
count = 1
while (n > 0):

	# Lê as entradas e transforma
	# o tipo das 10 primeiras em inteiro
    senhaFinal = []
    senhas = []
    linhas = []
    for e in range(n):
        linha = list(input().split())
        linhas.append(linha)
    for linha in linhas:
        for e in range(10):
            linha[e] = int(linha[e])

    
    # Adiciona uma lista de 12 números na lista "senhas"
    # para cada senha dada em letras na entrada
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

    # Confere os elementos de cada senha de 2 em 2 e guarda
    # aquele que se repete n vezes na lista "senhaFinal"
    for e in range(0, 12, 2):
        nums = []
        for senha in senhas:
            nums.append(senha[e])
            nums.append(senha[e + 1])
        for num in nums:
            if (nums.count(num) == n):
                senhaFinal.append(num)
                break

    
    # Imprime a saída com a senha formatada
    print("Teste %d" % count)
    for d in senhaFinal:
        print(d, end="")
        print(" ", end="")
    print()
    print()
   
    # Lê um novo valor para n
    # Implementa o contador
    n = int(input())
    count += 1