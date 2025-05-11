E, P = map(int, input().split())
td = 0 #total de danos

for i in range(P): 
    d = P-i #aqui subtrai i no P, tipo 30-1, 30-2...
    td += d #faz a sominha fofinha 
    if td >= E: # aqui eh quando a guerra começa
        print(i+1)
        break
else:
    print("F")