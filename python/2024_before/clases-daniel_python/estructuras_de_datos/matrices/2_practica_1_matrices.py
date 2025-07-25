import pdb
fila= 4
columna=4
matriz=[]

for f in range(fila):
	matriz.append([])
	for c in range(columna):
		matriz[f].append("hola")

for p in range(fila):
	for n in range(columna):
		pdb.set_trace()
		matriz[p][n] = 1


for x in matriz:
	print(x)

		# (0,0) (0,1) (0,2) (0,3) 
		# (1,0) (1,1) (1,2) (1,3)
		# (2,0) (2,1) (2,2) (2,3)


# none none
# none none 

# 1 2
# 3 4

# (0,0) (0,1)
# (1,0) (1,1)


# 1 2 3  4  5 6
# 7 8 9 10 11 12 
# 13 14 15 16 17
	




	



