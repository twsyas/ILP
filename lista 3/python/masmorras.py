N = int(input())
lv = 1
a = 0
for i in range(N):
    char,q = input().split()
    q= int(q)
    char = str(char)
    
    if char == "t":
        if q == 1 or q == 2:

            lv = lv+q
            
        elif lv >=5: 
            print("Aventura concluída")
            break
    
    elif char == "b":
        if q== 1 or q == 2:
           lv = lv-q
           if lv <= 0:
                lv == 0            
    elif char == "m":
        f = q
        if f != 0 :
            a = 1
            print("Combate iniciado")
            if lv<f:
                print("Derrota! Fim da aventura")
                break
            elif lv>=f:
                print("VITÓRIA")
                lv=lv+1
                if lv>= 5:
                    print("Aventura concluida")
                    break
if lv < 5 and a == 0:
    print()



