import ast

def busqueda_lineal(lista,num):
	lista_no_string=ast.literal_eval(lista)
	for espacio in range(len(lista_no_string)):
		if lista_no_string[espacio]==num:
			print(f"el numero {num} esta en la posicion {espacio} de la lista {lista_no_string}")
		else:
			print ("no se encontro el numero que coloco en la lista")

def main():
	lista=input("escriba la lista: ")
	num=int(input("diga el numero que quiere buscar de la lista que coloco: ")
	busqueda_lineal(lista,num)

if __name__== '__main__':
	main()