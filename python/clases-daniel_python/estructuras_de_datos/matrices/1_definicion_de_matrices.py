from os import system 
import pdb
system("cls")

"""
matriz 5X5
			Columnas
           0 1 2 3 4 
		0| 1 2 3 4 5 |
		1| 4 5 6 7 8 |
Filas	2| 8 3 4 1 2 |
		3| 0 9 8 7 6 |
		4| 4 3 6 2 4 |

"""


"""
matriz 5X5
			Columnas
            0    1    2    3    4    5   
		0| 0,0  0,1  0,2  0,3  0,4  0,5|
		1| 1,0  1,1  1,2  1,3  1,4  1,5|
fileas	2| 2,0  2,1  2,2  2,3  2,4  2,5|
		3| 3,0  3,1  3,2  3,3  3,4  3,5|
		4| 4,0  4,1  4,2  4,3  4,4  4,5|
		5| 5,0  5,1  5,2  5,3  5,4  5,5|

"""

# ---------------primera form---------------
# listas dentro de una lista 
matriz = [[],[]]
print(matriz)
# [[], []]

print("----------------------------------------------------------------------------------------------")

matriz = [[1,2,3],[3,4,5],[5,6,7]]

filas = 5
columnas = 5

matriz = []
for i in range(filas):
	matriz.append([])

	for j in range(columnas):
		matriz[i].append(None)

for x in matriz:
	print(x)

print("--------agregar un uno a cada valor de la matri--------")
for i in range(filas):
	for j in range(columnas):
		matriz[i][j] = 1	

for x in matriz:
	print(x)

for i in range(filas):
	for j in range(columnas):
		print(matriz[i][j], end=" ")
	print()


