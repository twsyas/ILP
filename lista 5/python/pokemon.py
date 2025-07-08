N, m = [int(T) for T in input().split()]
pokedex = []
quant = []
for l in range(N):
    linha = [int(T) for T in input().split()]
    pokedex.append(linha)
P = int(input())
for i in range(N):
    for j in range(m):
        if pokedex[i][j] == P:
          quant.append(P)

#print(pokedex)
print(f"Ash pegou {len(quant)} pokemon")