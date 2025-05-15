def suma(a,b):
	return a+b

print (suma(1,2))

sum =  lambda a,b:a+b
print (sum(1,2))

print("===============================================")


#Si es una función que solo queremos usar una vez, 
#tal vez no tenga sentido almacenarla en una variable. 
# Es posible declarar la función y llamarla en la misma línea.

print( 
	 (lambda a,b:a+b)(2,4)
)
print("===============================================")

#Una función lambda puede ser la entrada a una función normal.
def mi_funcion(lambda_funcion):
	return lambda_funcion(2,3)

print( 
	 mi_funcion(lambda a,b:a+b)
)
print("===============================================")

#argumentos con valor asignado por defecto.
print(
	(lambda a,b,c=5:a+b+c)(2,4)
)



x = lambda a, b: (b, a)
print(x(3, 9))

def cuadrado(n):
	return n**2
print(cuadrado(3))

print("===============================================")
cua = lambda n:n**2
print(
	cua(3)
)
print("===============================================")

iter = [1,2,3,4,54,6,65,4,3]
# map(fun, iter)
cuadrados = list(map(lambda x:x**2, iter))
print (
	cuadrados
)

enteros = [1,2,3,4,5,6]
cuadrados=[]
for item in enteros:
	cuadrados.append(item**2)

print(cuadrados)

asf = list(map(lambda x:x**2,enteros))
print(asf)
print("===============================================")


valores = [1,2,3,4,5,6,7,8,9,10]
pares = []
for item in valores:
	if (item%2 == 0):
		pares.append(item)
		
print(pares)
paress =  list(filter(lambda x: x%2 ==0,valores) )
print(paress)
print("===============================================")

valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el
print(suma)

from functools import reduce
sumaa = reduce(lambda x, y: x + y, valores)
print(sumaa)
21