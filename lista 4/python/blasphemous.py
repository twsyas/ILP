N = int(input())
X = list(map(int, input().split()))
M = int(input())
vida = M

for i in X:
    
    if vida !=0 and vida>0:
        if i == 0:
            continue
        elif i == 1:
            vida = M
        else:
            vida = vida - i
    else:
        break
    
if vida>0:
    print("Yes, you can")
elif vida <=0:
    print("You Died")
