"""
TTT

El usuairo debe ingresar el numero de repeticiones 
que se deben hacer. dados diez numeros, calcular la cantidad de números
pares, la suma de los impares, el promedio 

1. Pedir la cantidad de números
2. Hacer un ciclo en donde se coloque los numeros
3. Agregarlos a una lista vacia
4. Determinar la cantidad de números pares que hay en la lista
	for
	lista
	if x%2==0
	num=num+1
5. Hacer la suma de los números impares que contenga la lista
6. Generar el promedio ue contenga la lista 
7. Retornar el resultado
"""
def lista():
	revision=True
	while revision:
		cantidad=input("cuantos numeros quiere colocar: ")
		if cantidad.isdigit():
			revision=False
		else:
			print("esto no es un numero")

	lista_nueva=[]
	

	for x in range(int(cantidad)):
		revision2=True
		while revision2:
			num=input("coloque los numeros que va usar para la lista: ")
			if num.isdigit():
				revision2=False
			else:
				print("esto no es un numero")
		lista_nueva.append(int(num))
	return lista_nueva
 
def calcular():
	lista_de_datos = lista()
	print(lista_de_datos)

	total_pares=0
	suma=0
	sumtodo=0

	for y in lista_de_datos:
		if y%2 == 0:
			total_pares+=1
		else:
			suma=suma+y
		sumtodo=sumtodo+y

	promedio=sumtodo/len(lista_de_datos)

	print("en total hay",total_pares,"pares en la lista")
	print("la suma de todo los impares da",suma,"y el promedio de la lista es igual a",promedio)


def main():
	calcular()


if __name__=='__main__':
	main()
