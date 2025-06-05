S, N = map(int,input().split())
Z = [0]*N #lista de zeros
for i in range(S):
    P = int(input())
    for j in range(N):
        if j%P == 0:
            Z[j] = 1
            
print(*Z)

## pulo de sapos
# 0 = nao pisou
# 1 = pisou
# N = numero de pedras
# P = numero de pulos
# N/P = quantidade de pedras pisadas
# N % P != 0 pedra pisada