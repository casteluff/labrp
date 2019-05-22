n = int(input())

count = 1
while (n > 0):
  player1 = input()
  player2 = input()

  print("Teste %d" % count)
  for e in range(n):
    hands = list(map(int, input().split())
    if ((hands[0] + hands[1]) % 2 == 0):
      print(player1)
    else:
      print(player2)

  count += 1