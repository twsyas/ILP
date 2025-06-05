N = int(input())
caixa = []

for i in range(N):
    el = map(int, input().split())
    caixa.extend(el)
    break

x = int(input())

if x in caixa:
    print(x)
else:
    print(-1)