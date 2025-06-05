#m =[
   # [2, 3. -1, 5],
  #  [1, -2, 3, 4],
 #   [4, -5, 6, 7]
#]

#print(m[2][1]) #primeira posiçao representa a linha que vc quer acessar e a segunda linha, a coluna

linhas = 3
colunas = 4
matriz = []
for l in range(linhas):
    lista = []
    for c in range(colunas):
        lista.append(0)
    matriz.append(lista)
print(matriz)

linhas = 3
colunas = 4
matriz = []
for l in range(linhas):
    matriz.append([0]*colunas)
print(matriz)

linhas = 3
colunas = 4
matriz = [[0]*colunas for l in range(linhas)]

## o custo para percorrer uma matriz quadrática inteira é n²;
### arvore de jogo / programação dinâmica / arvore binária

