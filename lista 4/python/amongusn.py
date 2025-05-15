N=int(input())
l1=list(map(int,input().split()))
a=1
for i in range(len(l1)-1):
        if a==0:
            break
        if l1[i]<=l1[i+1]:
            l1[i+1],l1[i]=l1[i],l1[i+1]

        for j in range(len(l1)-1):
            if l1[j+1]<=l1[j]:
                l1[j+1],l1[j]=l1[j],l1[j+1]
                a=1


print(*l1)