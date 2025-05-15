N=int(input())
l1=list(map(int,input().split())).sort()
#a=1
for i in range(len(l1)):

        for j in range(0, len(l1)-i-1):
            if l1[j+1]<l1[j]:
                l1[j], l1[j+1]=l1[j+1],l1[j]
                #a=1


print(*l1)

