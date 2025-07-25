class matriz:
	def __init__(self,altura,ancho):
		self.altura=altura
		self.ancho=ancho

sup=0
inf=0
matriz_c=[]
intancia_matriz=matriz(5,5)

for i in range(altura):
	matriz_c.append([])
	for j in range(columnas):
		matriz_c[i]=int(input("diga los numeros: "))



for i in range(len(matriz_c)):
	for j in range(len(matriz_c)):
		if i<j:
			sup+=matriz[i][j]
		elif i>j:
			inf+=matriz[i][j]

if superior>inferior:
	print('s')
elif superior<inferior:
	print('i')
else:
	print('n')
