## Criando uma matriz 7x7
matriz = []
for i in range(7):
    linha = list(map(int, input().split()))
    matriz.append(linha)

## contador de peças em um jogo
contador = 0
for i in range(7):
    for j in range(i + 1):  # j vai de 0 até i (inclusive diagonal)
        if matriz[i][j] == 1:
            contador += 1

print(contador)

###### REVER ESTE CODIGO PQ NAO SEI SE TA CERTO