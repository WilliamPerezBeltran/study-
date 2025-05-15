
n = 4
fila = n
columna = n 
matriz = []

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append("O")


for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		print(matriz[i][j], end = '')
	print("") 

myArray = [1,2,-1,1,0,1,2,-1,-1,-2]

horizontal = True
avanzarHorizontal = 1

for data in myArray:
	if horizontal:
		avanzarHorizontal*=data
		for j in range(avanzarHorizontal):
			if avanzarHorizontal>0:
				matriz[i][j] = "X"

			else:
				pass
		horizontal = False
	else:
		pass
		# for i in range(data):
		# 	print(matriz[i][j], end = '')
		# print("") 
		# horizontal = True

