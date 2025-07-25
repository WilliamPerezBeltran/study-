#!/usr/bin/python -tt
# coding=utf-8



"""
Generadores:
Son funciones que nos permitirán obtener sus resultado 
poco a poco.
Es decir , cada vez que llamemos a la función nos darán un nuevo 
resultado.

Para que sirven:
Generan datos en tiempo de ejecución

Cómo se contruyen:
Para construir generadores sólo tenemos que usar la orden yield.
Esta orden devolverá un valor (igual que hace return) pero además.
Congelará la ejecución de la función hasta la próxima vez que le pidamos un valor.
"""

print "-------------ejemplo 1-------------"
generadores = (x for x in range(20))
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print next(generadores)
print "-----------------------------------"



def generador(maximo):
	n = 0
	while n < maximo:
		yield n
		n+=1

for dato in generador(20):
	print dato

