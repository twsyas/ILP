continua = 1
while continua != 0:
	media = 0
	for j in range(7):
		d=float(input())
		media = media+d
	media = media/7.0
	if media>15.0:
		print("Quente!")
	else: 
		print("Frio!")
	continua = int(input())