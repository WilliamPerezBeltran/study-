def funcion():
    return 5

def generador():
    yield 5

print(funcion())
print(generador())

a = generador()
print(next(a))

print("======================================")

def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

g = generador()
print(next(g))
print(next(g))
print(next(g))

print("======================================")

lista = [1,2,3,4,5,6]
al_cuadrado = [x**2 for x in lista]
print(al_cuadrado)


al_cuadrado_generador= (x**2 for x in lista)
for i in al_cuadrado_generador:
    print(i)

print("======================================")


def primerosn(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums
    
print(sum(primerosn(10000000)))

print("===============")


def primerosn(n):
    num = 0
    for i in range(n):
        yield num
        num += 1
print(sum(primerosn(10000000)))

