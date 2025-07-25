import sys 
import pdb
import ast
def busqueda_lineal(lista_nueva,dato):
	lista_lineal = lista_nueva
	for posicion in range(len(lista_lineal)):
		if dato == lista_lineal[posicion]:
			return posicion
	return None


def busqueda(lista,dato):
	lista_nueva = ast.literal_eval(lista)
	dato = ast.literal_eval(dato)
	if busqueda_lineal(lista_nueva,dato) != None:
		print(f"el dato {dato} esta en la posicion {busqueda_lineal(lista_nueva,dato)}")
	else:
		print(f"el dato {dato} no se encontro el la lista {lista_nueva}")

def main():
	argumentos = sys.argv
	lista = argumentos[1]
	dato = argumentos[2]
	busqueda(lista,dato)

if __name__== '__main__':
	main()



a = [1,2,4,5,2,46,4,3,6,3,56,7,6,57,5,4,4]
