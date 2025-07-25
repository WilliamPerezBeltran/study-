# ***************
# Método de ordenamiento de burbuja 
# revisa cada elemento de la lista con el siguiente elemento, 
# intercambiandolos de posicion si esta en el orden equivocado
# ***************

# 4 2 6 8 5 7 
# 2 4 6 8 5 7 
# 2 4 6 8 5 7 
# 2 4 6 5 7 8
# 2 4 5 6 7 8 

# rr = [1,2,3,4,3,2,5,4,6,56,3,4,23,45,78,9,0,1,2,4,2,6,8,5,7]
rr = [4,2,6,8,5,7,0]
arr=range(len(rr))

for i in range(len(rr)):
	for x in range(i,len(rr)):
		if rr[i] > rr[x]:
			pivote = rr[i]
			rr[i] = rr[x]
			rr[x]= pivote

print(rr)