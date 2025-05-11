N, T= map(int, input().split())
for i in range(N):
    H = int(input())
    H+=H

## as condicionais precisam estar
    if H>T:
        print(i)
        break
    #else:
     #   print(0)