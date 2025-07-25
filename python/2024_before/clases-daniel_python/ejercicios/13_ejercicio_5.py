"""
lo mismo que 13_ejercicio_3 pro diferenciando en las posiciones impares
"""
import sys 
import ast

#sys.argv

def impares(a,b):
	lista1 = ast.literal_eval(a)
	lista2 = ast.literal_eval(b)

	if len(lista1)>=1 and len(lista1)<=100:
		
		diferentes=[]

		for p in range(len(lista1)):
			
			if (p+1)%2!=0:

				if lista1[p] != lista2[p]:
					diferentes.append(p+1)

		if diferentes==[]:
			return("todas las posiciones impares son iguales")

		else:
			return("las posiciones impares:",diferentes,"son diferentes")

	else:
		print ("estos valores no se permiten")


	
def main():
	args = sys.argv[1:]
	print((args))
	


	print(impares(args[0],args[1]))

if __name__=='__main__':
	main()