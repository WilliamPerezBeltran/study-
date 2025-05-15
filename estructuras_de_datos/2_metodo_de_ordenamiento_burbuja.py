"""

Método de ordenamiento burbuja

Revisa cada elemento de la lista 
con el siguiente elemente intercambiando los elementos de posicion 
si estan en el orden equivocado

Ejemplo

4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8

este ordenamiento no estan eficiente pero es bueno para estudiarlo
"""

# lista = [44,42,56,86,52,17]
lista = [4,2,6,8,5,7]

print("array para ordenar = %s"%(str(lista)) )

def swap(mayor, menor):
	pivote = mayor
	lista[x] = menor
	lista[x+1] = pivote

for i in range(len(lista)):
	for x in range(len(lista)-1):
		if lista[x] > lista[x+1]:
			swap(lista[x],lista[x+1])
			print(lista)


print("array ordenado = %s"%(str(lista)) )

