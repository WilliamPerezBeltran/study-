
def fib2(n): # devuelve la serie de Fibonacci hasta n
	"""Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
	result = []
	a, b = 0, 1
	while a < n:
	result.append(a)
	# ver abajo
	a, b = b, a+b
	return result

f100 = fib2(100)
# llamar la funcion 
print(f100)
# escribir el resultado
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
Este ejemplo, como es usual, demuestra algunas características más de Python:
• La sentencia return devuelve un valor en una función. return sin una expresión como argumento retorna None. Si
se alcanza el final de una función, también se retorna None.
• La sentencia result.append(a) llama a un método del objeto lista result. Un método es una función que
'pertenece' a un objeto y se nombra obj.methodname, dónde obj es algún objeto (puede ser una expresión), y
methodname es el nombre del método que está definido por el tipo del objeto. Distintos tipos definen distintos
métodos. Métodos de diferentes tipos pueden tener el mismo nombre sin causar ambigüedad. (Es posible definir tipos
de objetos propios, y métodos, usando clases, mirá Clases). El método append() mostrado en el ejemplo está
definido para objetos lista; añade un nuevo elemento al final de la lista. En este ejemplo es equivalente a
result = result + [a], pero más eficiente.


Un método es una función que 'pertenece' a un objeto y se nombra obj.methodname, dónde obj es algún 
objeto (puede ser una expresión), y methodname es el nombre del método que está definido por el tipo
del objeto.

"""