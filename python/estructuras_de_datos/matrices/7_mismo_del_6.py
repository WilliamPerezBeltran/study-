"""
(50%) Se define que una matriz cuadrada N x N puede estar orientada hacia su triángulo
superior o hacia su triángulo inferior.
Está orientada hacia su triángulo superior si la suma de los valores contenidos en dicho
triángulo son superiores a la suma de los valores contenidos en el triángulo inferior. De la
misma manera se dice que está orientada hacia su triángulo inferior si la suma de los valores
contenidos en dicho triángulo son superiores a la suma de los valores contenidos en el triángulo
superior. Si las sumas son iguales se dice que la matriz no tiene orientación. Los triángulos
están separados por la diagonal principal de la matriz, la cual no forma parte de ninguno de los
triángulos.
En el ejemplo mostrado, los números en azul constituyen el triángulo superior y los números en
rojo el triángulo inferior.

[9,2,2,2]
[2,8,2,2]
[2,2,7,2]
[2,2,2,6]
Escriba una función llamada triangulos que retorne si una matriz cuadrada dada, está orientada
hacia su triángulo superior (‘s’), hacia su triángulo inferior (‘i’) o no tiene orientación (‘n’). Se
conoce el tamaño N de la matriz.



"""






# valor suministrado 5
# resultado 5 4 4 3 3 3 2 2 2 2 1 1 1 1 1

import os 
import pdb
os.system("clear")

def triangulos(matriz):

	orientacion_tuple = (
		('s','superior'),
		('i','inferior'),
		('n','sin orientacion'),
	)
	superior = 0
	inferior = 0
	orientacion_rta = None

	for index_i,i in enumerate(matriz):
		for index_j, j in enumerate(matriz[index_i]):
			if index_i < index_j:
				superior+=matriz[index_i][index_j]
			elif index_i > index_j:
				inferior+=matriz[index_i][index_j]

	if superior > inferior:
		orientacion_rta = 's'
	elif superior < inferior:
		orientacion_rta = 'i'
	else:
		orientacion_rta = 'n'

	for tuple_index in range(len(orientacion_tuple)):
		if orientacion_tuple[tuple_index][0] == orientacion_rta:
			return orientacion_tuple[tuple_index][1]


ejemplo_matriz_orientacion_superior = [[1,20,3,4],[5,6,7,80],[8,7,6,50],[4,3,2,10]] #la rta da matriz superior
ejemplo_matriz_orientacion_inferior = [[1,2,3,40],[50,6,8,90],[80,70,6,50],[40,300,20,10]] #la rta da matriz inferior
ejemplo_matriz_sin_orientacion = [[9,2,2,2],[2,8,2,2],[2,2,7,2],[2,2,2,6]] #la rta da matriz sin orientacion


def main():
	print
	print(f"La matriz es de tipo 'matriz {triangulos(ejemplo_matriz_sin_orientacion)}'")

if __name__=='__main__':
	main()
