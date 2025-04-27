X,Y = map(int, input().split())
if(X <= 0 or X >= 100) or (Y <= 0 or Y >= 100):
  print("Coordenada invalida")
else:
  if(X>=71 or Y>=71):
    print("Coordenada valida e o navio esta longe")
  else:
    print("Coordenada valida e o navio esta perto")

