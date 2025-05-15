"""
ver si los valores ubicados en las posiciones pares de una lista son todos iguales

con listas hasta de tamaño 100
"""
def pares():

	tamano=int(input("que tan grande es la lista: "))

	if tamano>=1 and tamano<=100:
		
		arr1=[]
		arr2=[]

		for v in range(tamano):

			v1=int(input("coloque los valores para la lista 1: "))
			arr1.append(v1)

			v2=int(input("coloque los valores para la lista 2: "))
			arr2.append(v2)
			
		diferentes=[]

		for p in range(tamano):
			
			if (p+1)%2==0:
			
				if arr1[p] != arr2[p]:
					diferentes.append(p+1)

		if diferentes==[]:
			return("todas las posiciones pares son iguales")

		else:
			return("las posiciones pares:",diferentes,"son diferentes")

	else:
		print ("estos valores no se permiten")



def main():
	print(pares())

if __name__=='__main__':
	main()