# iterable, iterator
print("""
Con los iteradores hay varios conceptos interesantes que hasta ahora caigo en cuenta que son muy 
importantes. 

Los primero es la definición de objectos iterables esto quiere decir objectos en donde se puede 
recorrer los elementos. Objectos como listas, rangos, diccionarios, etc. 
Ahora, podemos decirlo de una forma mas tecnica: 
Un iterable es un objecto que implemente el método __iter__() y va retornar un iterator. 
iterator => un objecto que implementa el metodo __iter__() y __next__().

Protocolo iterable:
Es un conjunto de reglas que hace que un objecto se pueda usar en un for o , en 
list(), sum(), etc :
Las dos piezas del protocolo son: 

    - definicion de "iterable o iterable" => objecto que implemente los metodso especiales 
    __iter__() y este metodo es decir el metodo __iter__() debe devolver un iterator:
    
    - Definicion de iterator: => Objeto que implemente __iter__() y __next__()
    __iter__(): devuelve el propio iterador  yl
    __next__(): devuelve el siguiente valor y lanaza StopOteration cuan ya no hay mas elementos que recorer 


Y lo otro que considero importante es el concepto de eager y lazy:

lazy iteration o iteracion perezosa quiere decir que no compute todo a la vez solo se debe producir 
los valores o los datos a iterar cuando sean necesarios, esto lo que produce es que ahorra memoria y puede manejar infinitas secuencias.

Eager loading carga los datos de una sola lo que implica que todo lo guarda en memoria.
""")

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~ otro ejemplo ~~~~~~~~~~~~~~~")
# Example: Eager vs Lazy
# Eager
nums = [x*x for x in range(1_000)]
print(nums)
 
print("~~")
# lazy
nums_ = (x*x for x in range(1_000))
print(next(nums_))

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~ otro ejemplo ~~~~~~~~~~~~~~~")
# Example: Eager
for x in range(2,7):
    print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("==========~~~~~~~~~~~")
print("~~~~~~~~~~ otro ejemplo ~~~~~~~~~~~~~~~")
# Example: Lazy

a = [1,2,3,4,5,6]
b = iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

print("==========~~~~~~~~~~~")
print("~~~~~~~~~~ otro ejemplo ~~~~~~~~~~~~~~~")

class Counter():
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin  

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual > self.fin:
            return StopIteration
        valor = self.actual 
        self.actual += 1
        return valor  


c = Counter(20,28)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("~~~~~~~~~~ otro ejemplo ~~~~~~~~~~~~~~~")
class CountDown:
    def __init__(self, start):
        self.current = start 

    def __iter__(self):
        return self  # el objeto es su propio iterador
   
    # - Returna el estado actual 
    #- Prepara el objecto para generar el siguiente elemento
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current 
        self.current -= 1
        return value 

# Uso 
for num in CountDown(10):
    print(num)

print("~~~~~~~~~~ otro ejemplo. ~~~~~~~~~~~~~~~")
x = CountDown(10)
print(next(x))
print(next(x))

print("~~~~~~~~~~~~~~~~~~~~~~~~~")

aa = [99,88,77]
it = iter(aa)
print(next(aa))
print(next(aa))

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
