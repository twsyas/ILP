qtd_avaliacoes_por_nota = [0] * 6
notas = map(int, input().split())
for nota in notas:
   qtd_avaliacoes_por_nota[nota] += 1
for nota in range(1, 6):
   qtd = qtd_avaliacoes_por_nota[nota]
   print('Nota', nota, "-", qtd)
