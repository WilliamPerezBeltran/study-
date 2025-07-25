import pdb;
# arr = [5,12,15,30,50,65]
arr = [5,12,15,30,50,65,68,78,98,100,110,120,140,170]

def busquedaBinaria(dato):
	izquierda = 0
	derecha = len(arr)-1
	

	while izquierda <= derecha:
		centro = (izquierda + derecha)//2
		if dato == arr[centro]:
			return centro
		elif dato < arr[centro]:
			derecha = centro -1
		elif dato > arr[centro]:
			izquierda = centro +1

	return None


def busqueda(dato):
	if busquedaBinaria(dato) == None:
		print("el número %d no se encontro"%(dato))
	else:
		print("el número %d esta en el índice %d "%(dato,busquedaBinaria(dato)))



print(busqueda(100))