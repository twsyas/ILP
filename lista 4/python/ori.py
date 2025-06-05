M = int(input())
N = int(input())
X = list(map(int, input().split()))
B = list(map(int,input().split()))
XP = 0
for i in range(len(X)):
    XP = XP+(X[i]*B[i])

if XP>=M:
    print("Upou de Nivel!")
elif XP<M:
    print("Nao foi dessa vez!")
