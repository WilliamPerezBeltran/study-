import pdb
from copy import copy, deepcopy

myArray = [13,12,4,3,15]
pivote = True
data = None
for x in myArray:
	if pivote:
		data = x
		pivote = False
	else:
		if x < data:
			data =x

# return data
print(data)
# ==============================

n = 5
fila = n
columna = n 
matriz = []

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append(None)

pivote = True
for i in range(len(matriz)):
	# pdb.set_trace()
	for j in range(len(matriz[i])):
		if pivote:
			matriz[i][j] = "X"
			pivote = False
		else:
			matriz[i][j] = "_"
			pivote = True

# for x in matriz:
# 	print(x)

for i in range(len(matriz)):
	# pdb.set_trace()
	for j in range(len(matriz[i])):
		print(matriz[i][j], end = '')
	print() 
# ==============================
print() 
print() 
print() 

print(""" 
Pregunta 3
Escribir un programa utilizando Python que encuentre los dos elementos del arreglo que sumados dan 10. Se deben imprimir ambos números como resultado separados por un espacio (en el orden en que aparecen en el arreglo).

Por ejemplo, para el arreglo (1,3,4,2,7,0) el resultado seria: 3 7
""")



# myArray = [ 1,3,4,2,7,0 ]
# # pdb.set_trace()

# for x in range(len(myArray)):

# 	# newArray = myArray
# 	# newArray = myArray
# 	newArray = deepcopy(myArray)
# 	try:
# 		newArray.pop(x) 
# 	except Exception as e:
# 		pdb.set_trace()
	
	
# 	for y in newArray:
# 		if myArray[x]+y == 10:
# 			print("%d %d"%(myArray[x],y))
# 			print()


# 			# print("entro") 
# 			# pdb.set_trace()


myArray = [ 1,3,4,2,7,0 ]
pivote = True
for x in range(len(myArray)):
	newArray = deepcopy(myArray)
	newArray.pop(x) 
	
	for y in newArray:
		if myArray[x]+y == 10 and pivote:
			print("%d %d"%(myArray[x],y))
			pivote = False


			# print("entro") 
			# pdb.set_trace()

print(""" 
Pregunta 4
Se tiene una X en la esquina superior izquierda de 
un área de 4x4. Se tiene una matriz con 10 elementos. 
Cada 2 elementos de la matriz corresponden a un movimiento, 
el primero en el eje horizontal y el segundo en el eje 
vertical. El numero indica las unidades a moverse y el 
signo la dirección (positivo para derecha o abajo, 
negativo para izquierda o arriba)

Por ejemplo, para la matriz myArray:=(1,2,-1,1,0,1,2,-1,-1,-2)

La X se moverá una unidad a la derecha y dos hacia abajo, luego una unidad a la izquierda y una abajo y así sucesivamente. El programa a escribir debe imprimir la posición final de la X. Para representar los lugares donde la X no se encuentra utilizar la letra O. Si la instrucción obliga a la X a salir del área de 4x4 la X permanecerá en el borde, sin salir. Para el arreglo presentado el resultado se vería así:

OXOO
OOOO
OOOO
OOOO

""")
n=4
fila = n
columna = n 
matriz = []

for i in range(fila):
	matriz.append([])
	for j in range(columna):
		matriz[i].append(None)
		
pivote = True
for i in range(len(matriz)):	
	for j in range(len(matriz[i])):
		if pivote:
			matriz[i][j] = "X"
			pivote = False
		else:
			matriz[i][j] = "_"
			pivote = True

for i in range(len(matriz)):	
	for j in range(len(matriz[i])):
		print(matriz[i][j], end = '')
	print() 
