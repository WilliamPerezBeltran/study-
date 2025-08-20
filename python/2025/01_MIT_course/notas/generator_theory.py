"""
un generator es un funcion que devuelve un iterator (recuerde que un iterator es un objeto que 
tiene el dos metodos especiales __iter__ y el __next__) que produce valores "uno a la vez"
usando yield en lugar de return 

A diferencia de una lista, no guarda todos lo valores en memoria. 
"""

def my_generator():
        yield 1
        yield 2
        yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

print("~~~~~~~~~~~~~~~~~~~~")

def cuadrados(n):
    for x in range(0,n+1):
        yield x * x 

for x in cuadrados(4):
    print(x)

print("~~~~~~~~~~~~~~~~~~~~")
l = [x+5 for x in range(4)] 
print(l)

print("~~~~~~~~~~~~~~~~~~~~")
s = (x for x in range(5))
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
