


lista = [12,23,34,45,56,67,1,3,6,3,6,3,999]

def buqueda_lineal(dato):

	for x in range(len(lista)):
		if lista[x] == dato:
			return x
	return None


def buscar(dato):

	if buqueda_lineal(dato) != None:
		print("el dato {} se encontro en la posicion {} ".format(dato,buqueda_lineal(dato)))


for x in range(len(lista)):
	print("lista[%d] = %d "%(x,lista[x]))

buscar(dato=999)