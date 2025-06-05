N, T= map(int, input().split())
a = 0
b = 0
x = 0
for i in range(1,N+1):
    H = int(input())
    x = x+H

    if x>T and a==0:
        b=i-1
        a=1
    
    elif x<=T and a==0:
        b=i
        
print(b)
    #else:
     #   print(0)