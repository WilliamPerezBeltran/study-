import os
import pdb
os.system("clear")
matriz=[]

print("********primero se inicializa la matriz*************")
print()

matriz =[]
fila = 8
columna = 8

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append(None)

print()
for x in matriz:
	print(x)
print()
print("*********segundo se muestra sus posiciones************")
print()

for i in range(fila):
	for j in range(columna):
		matriz[i][j] = (i,j)

print()

for i in range(fila):
	for j in range(columna):
		print(matriz[i][j],end=" ")
	print()
print()
print("*********tercero se rellenan su diagonal************")
print()

for i in range(fila):
	for j in range(columna):
		if i == j:
			matriz[i][j] = 1
		else:
			matriz[i][j] = 0

print()

for x in matriz:
	print(x)

