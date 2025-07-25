filas=5
columnas=5
matriz=[]

for i in range(filas):
	matriz.append([])
	for j in range(columnas):
		matriz[i].append(None)

for x in matriz:
	print(x)


for i in range(filas):
	for j in range(columnas):
		print((i,j),end="")
	print()

# i i  j
#       0      1      2      3      4 
# 0|(0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
# 1|(1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
# 2|(2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
# 3|(3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
# 4|(4, 0) (4, 1) (4, 2) (4, 3) (4, 4)

# 1000
# 0100
# 0010
# 0001


for i in range (filas):
	for j in range (columnas):
		if i == j:
			matriz[i][j]=1
		else:
			matriz[i][j]=0

for x in matriz:
	print(x)

