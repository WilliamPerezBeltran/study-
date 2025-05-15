"""
busqueda binaria 

Calcular el punto meido con el dato a buscar 
si es igual el dato al punto medio retornar indice 
si el dato a buscar es mayor que el punto medio, izquierda es igual al valor del medio +1
si el dato a buscar es menor que el punto medio, derecha es igual al valor del medio -1
se seguira ejecutando siempre y cuenado izquierda sea menor o igual a derecha 

"""

a =[5,12,15,30,50,65,100,102,103,105,148,159,168,200]
print(a)


import pdb

def buscar(dato):
	i = 0
	d = len(a)-1
	pm = (i+d)//2
	while (a[pm] != dato and i <= d):
		if a[pm] > dato:
			d = pm-1
			pm =(i+d)//2
		else:
			i = pm+1
			pm =(i+d)//2

	return "el valor %d está en la posicion %d de la lista"%(dato,pm+1) if a[pm] == dato else "el valor %d no esta en la lista"%(dato)



print(buscar(205))



