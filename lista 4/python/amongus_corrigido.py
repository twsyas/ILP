N = int(input())
ordem_kills = [0] * N
print(ordem_kills)
kills = list(map(int, input().split()))
ordem_kills_ = [(ordem_kills.insert(kills))] #  tá retornando None
print(ordem_kills_)

#for i in kills:
 #   ordem_kills[i] += 1 #faz a contagem de kills
for kills in range(0, N):
    ord_kills = ordem_kills[kills] # este era para ordenar as kills
    print(ord_kills)

    ## ver o slide da  aula de lista e vetores (pag. 31)

## outro código para verificar

#N = int(input())
#ordem_kills = [0] * N
#kills = map(int, input().split())
#ordem_kills = ordem_kills.append(kills)

#for i in kills:
 #   ordem_kills[i] += 1
#for i in range(0, N):
 #   ord_kills = ordem_kills[kills]
  #  print(ord_kills)