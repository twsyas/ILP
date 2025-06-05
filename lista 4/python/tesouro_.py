N = int(input())
A = list(map(int,input().split()))
S = int(input())

v = 0

for i in A:
    if i <= S:
        v += 1
    else:
        break

print(v)

if v == N:
    print(1)
else:
    print(0)