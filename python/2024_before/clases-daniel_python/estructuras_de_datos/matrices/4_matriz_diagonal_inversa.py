filas=5
columnas=5
matriz=[]

for i in range(filas):
	matriz.append([])
	for j in range(columnas):
		matriz[i].append(None)

for i in range(filas):
	for j in range(columnas):
		if i+j==filas-1 or i==j:
			matriz[i][j]=1
		else:
			matriz[i][j]=0

for x in matriz:
	print (x)

