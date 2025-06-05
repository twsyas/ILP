N = int(input())
A = []
for i in range(N):
    obs = map(int, input().split())
    A.extend(obs)
    break
S = int(input())

for j in range(len(A)):
    if S>=A[j]:
        A+=1
    else:
        print(0)
   