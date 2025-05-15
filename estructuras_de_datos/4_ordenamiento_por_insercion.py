"""

Ordenamiento por selección 
es un algoritmo que consiste en ordenar los elementos de manera acendente odescendente 

fucniamiento 
-Recorremos cada elemento de la a
-Cada ellemento de la a se ordena si a suizquirerda tiene un elemento mayor que el actual
-Si es correcto el paso anteiror, se hace el intercambio de valores
-El elemento se sigue recorriendo hacia la  izquierda hasta que tenga un elemento menor que el 


"""
import pdb
a = [10,4,6,5,8,7,1,0]
print(a)
print('----')

for i in range(1,len(a)):
	if a[i] < a[i-1]:
		for x in range(i,-1,-1):
			if  x>0 and a[x] < a[x-1]:
				pivote = a[x]
				a[x] = a[x-1]
				a[x-1] = pivote
	print(a)

