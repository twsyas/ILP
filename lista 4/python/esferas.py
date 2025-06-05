N = int(input())
E = list(map(int, input().split()))
esferas = []
for i in range(1,8):
    if i in E:
        esferas.append(i)

if len(esferas) == 7:
    print(*esferas)
    print("Saia Shenlong e realize o meu desejo")
else:
    print(*esferas)
    print("Nao encontramos todas")