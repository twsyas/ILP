# criando a matriz do terreno!!
N, m = [int(T) for T in input().split()]
Vl = []
for l in range(N):
    linha = [int(V) for V in input().split()]
    Vl.append(linha)

# criando o "input" de seleção para o usuário adicionar as entradas
selecao = input().split() 
tipo = selecao[0] # L ou C
X = int(selecao[1]) # transforma o segundo item da lista em inteiro

## Calculando a soma, conforme o escolhido pelo usuário
if tipo == "L": ## este looping calcula a linha conforme o indice escolhido pelo usuário
    soma = sum(Vl[X-1]) 
elif tipo == "C": ## este looping calcula a coluna conforme o indice escolhido pelo usuário
    soma = sum(Vl[i][X-1] for i in range(N))
 ### (caso as linhas acima estiverem confusas, revisar sobre listas)
print(soma)