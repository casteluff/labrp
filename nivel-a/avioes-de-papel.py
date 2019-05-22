e = list(map(int, input().split()))

suficiente = False
if (e[0] * e[2] <= e[1]):
    suficiente = True

if (suficiente):
    print('S')
else:
    print('N')