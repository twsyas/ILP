C, c, X = map(int, input().split())
if (C%c != 0):
    print("!eh possivel")
else:
    cubos = (C//c)**3
    if (cubos <= X):
        print("Eh possivel")
    else:
        print("!Eh possivel")