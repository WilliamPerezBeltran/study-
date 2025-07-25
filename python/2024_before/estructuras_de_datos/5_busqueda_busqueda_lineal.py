arr = [12,32,3,45,43,2,3,5,7,8,90,87,65,43,45,72,59,21]



def busquedaLineal(dato):
	for x in range(len(arr)):
		if dato == arr[x]:
			return x
	return None


def buscar(dato):
	if busquedaLineal(dato) == None:
		return "el dato %d no se encontro"%(dato)
	else:
		return "el dato %d se encontro en el indice: %d"%(dato, busquedaLineal(dato))


print(buscar(0))





for x in range(len(arr)):
	print("arr[%d] => %d"%(x,arr[x]))



