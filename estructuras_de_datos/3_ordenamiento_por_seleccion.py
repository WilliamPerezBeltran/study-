"""

Ordenamiento por selección 
es un algoritmo que consiste en ordenar los elementos de manera acendente odescendente 

fucniamiento 
-Buscar el dato mas pequeño de la lista
-Intercanbiarlo por el acutal 
-Seguir buscando el dato mas pequeño de la lista
-Intercambiarlo por el actual
-Esto se repetira sucecivamente

"""
lista = [10,2,3,4,11,3,4,100,5,6,7,8,9,0]
print(lista)

for i in range(len(lista)):
	for x in range(i,len(lista)):
		if (lista[i] > lista[x]):
			pivote = lista[i]
			lista[i] = lista[x]
			lista[x] = pivote

print(lista)

