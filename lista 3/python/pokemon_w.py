E, P = map(int, input().split())
r = E
a = P
num_a = 0
while r > 0 and a > 0:
    r -= a
    a -= 1
    num_a +=1
if r <= 0:
    print(num_a)
else:
    print("F")