import os
import pdb
os.system("clear")
matriz=[]

print("********primero se inicializa la matriz*************")
print()
fila = 8
columna = 8

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append(None)

for x in matriz:
	print(x)
print()
print("*********segundo se rellena la matriz************")
print()

contador = 0

for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		matriz[i][j] = contador
		contador+=1

for x in matriz:
	print(x)

print()


print()
print("*********tercero se quitan las comas************")
print()

contador = 0

for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		matriz[i][j] = contador
		contador+=1

for i in matriz:
	for j in i:
		print(j,end=" ")
	print()
	
	
print()

print()
print("*********se organiza para que quede bonito************")
print()

contador = 0

for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		matriz[i][j] = contador
		contador+=1

for i in matriz:
	for j in i:
		if j < 10:
			print(j,end="  ")
		else:
			print(j,end=" ")
	print()
	
	
print()
