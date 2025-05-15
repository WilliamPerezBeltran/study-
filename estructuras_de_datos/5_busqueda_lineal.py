"""
busqueda lineal 

-Recorrer cada elemento de la lista
- Ir comparando el elemento que se desea 
- Devolver el index del elemento encontrado


"""

a =[12,43,56,54,67,87,98,9,4,87]

def busquedaLineal(dato):
	for x in range(len(a)):
		if dato == a[x]:
			return x
	return None

def buscar(dato):
	if busquedaLineal(dato) == None:
		print("El elemento %d no se encontnro "%(dato))
	else:
		print("El elemento %d se encuentro \n en la posicion %d del arreglo \n %s"%(dato,busquedaLineal(dato)+1, str(a)))



buscar(67)



