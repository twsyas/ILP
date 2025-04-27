z,g = map(str, input().split())
d, c = map(str, input().split())
if(z == d):
    print("Driblado")
    if(c == g):
        print("Gol")
    else:
        print("...e o goleiro pega")
else:
    print("Bloqueado \n")