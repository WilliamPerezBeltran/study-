"""
Lista y for:
    - Crea una lista de números [10, 20, 30, 40] y recórrela con un for.
    - Imprime cada número.
"""
for x in [10, 20, 30, 40]:
    print(x)
"""
String iterable
    - Toma un string "Python" y recórrelo letra por letra usando for.
"""
for x in "Python":
    print(x)

"""
Diccionario iterable
    - Crea un diccionario {"a":1, "b":2, "c":3}.
    - Recorre solo las claves con un for.
"""
a = {"a":1, "b":2, "c":3}
for i, (key,value) in enumerate(a.items()):
    print(i, key, value)

for x in a.keys():
    print(x)

"""
Lista con next()
    - Crea lista = [5, 10, 15].
    - Convierte la lista en un iterador con iter(lista).
    - Imprime sus elementos usando next() una por una.
"""
a = [5, 10, 15]
iterator = iter(a)
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
String con iterador
    - Convierte "Hola" en un iterador y usa next() para imprimir cada letra.
"""
s = "Hola"
iterator_ = iter(s)
print(next(iterator_))
print(next(iterator_))
print(next(iterator_))
print(next(iterator_))

"""
Control de StopIteration
    - Haz un try/except para atrapar StopIteration cuando ya no queden elementos en el iterador.
"""
try:
    s = "items"
    iterator_ = iter(s)
    print(next(iterator_))
    print(next(iterator_))
    print(next(iterator_))
    print(next(iterator_))
    print(next(iterator_))
    print(next(iterator_))
    print(next(iterator_))
except StopIteration:
    print("fin de la iteración")


ss = "guacamayas"
iterator_ = iter(ss)

while True:
    try:
        print(next(iterator_) )
    except StopIteration:
        print("Fin de la iteración")
        break

"""
Clase iterable simple
    - Crea una clase MiLista que guarde una lista interna.
    - Implementa __iter__ para devolver un iterador de esa lista.
"""
class ClaseIterableSimple():
    def __init__(self,lista):
        self.lista = lista

    def __iter__(self):
        return iter(self.lista)

mi_lista_iterable = ClaseIterableSimple([100,200,300])
for x in mi_lista_iterable:
    print(x)

"""
Clase como iterador
    - Crea Contador con __iter__ y __next__ que devuelva los números del 1 al 5.
"""

class Contadorr():
    def __init__(self):
        self.actual = 1  
        self.final = 5 

    def __iter__(self):
        return self 

    def __next__(self):
        if self.actual > self.final:
            raise  StopIteration

        valor = self.actual
        self.actual += 1
        return valor 

contadorr = Contadorr()

for x in contadorr:
    print(x)

"""
* Explicación
    - __iter__() => devuelve el objeto mismo porque ya es un iterador.
    - __next__() => devuelve el siguiente valor y avanza el estado interno (self.actual).
    Cuando self.actual supera self.fin, lanza StopIteration para terminar el bucle for.
"""










