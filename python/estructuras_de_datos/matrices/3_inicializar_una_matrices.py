import pdb
matriz=[]

fila = 8
columna = 8

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append(None)

for x in matriz:
	print(x)
print("*********************")

contador = 0

for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		matriz[i][j] = contador
		contador+=1

for x in matriz:
	print(x)
print("*********************")
for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		matriz[i][j] = (i,j)
		contador+=1

for x in matriz:
	print(x)
print("*********************")
fila = 8
columna = 8 
matriz = []

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append(None)

for i in range(len(matriz)):
	# pdb.set_trace()
	for j in range(len(matriz[i])):
		if i == j:
			matriz[i][j] = 1
		else:
			matriz[i][j] = 0


for x in matriz:
	print(x)





