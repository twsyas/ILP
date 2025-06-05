N = int(input())
l1 = list(map(int, input().split()))

while True:
    trocou = False
    for j in range(len(l1) - 1):
        if l1[j + 1] < l1[j]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
            trocou = True
    if not trocou:
        break

print(*l1)
