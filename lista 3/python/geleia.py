N = int(input())
trad = 0
ge = 0
for i in range(N):
    c =int(input())
    if c == 10:
        trad +=1
    if c ==11: 
        ge +=1
if trad > ge:
    print("Tradicional")
else:
    print("Geleia")

