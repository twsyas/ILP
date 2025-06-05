N=int(input())
l1=list(map(int,input().split()))
while True:
    ordem = False
    for j in range(len(l1)-1):
            if l1[j+1]<l1[j]:
                l1[j], l1[j+1]=l1[j+1],l1[j]
                ordem = True
    if ordem == True:
        break

print(*l1)