a = [1,2,3,4,5,6,456]

# print the value 
for x in a:
    print(f"value: {x}")

for index, value in enumerate(a):
    print(f"index: {index}, value: {value}")

print("~~~~~~~~~~~~~~")
print("   table       ")
print("index  value ")

for index, value in enumerate(a):
    print(f"{index}      {value}")



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
lista = [10, 15, 20, 25, 30]
nueva_lista = [x for x in lista if x > 20]
print( nueva_lista)
a = [10,20,30,40,50]
b = [1,2,3,4,5]
c = zip(a,b)
print(list(c))
print(c)

for x in zip(a,b):
    print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# metodos 
"""
x es el valor que queremos agregar 
i es el indice

append(x)
extend(iterable)
insert(i,x)
remove(x)
clear()
index(x)
count(x)
sort()
reverse()
copy()
"""
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

numbers = [1, 2, 3, 4, 5]
squares = [x**x for x in numbers ]
even_squares = [x**x for x in numbers if x%2 == 0]

print(squares)
print(even_squares)


words = ["hello", "world", "python"]
transformation = [ x.upper() for x in words ]
print(transformation)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
colors = ["red", "green"]
objects = ["car", "house"]

for x in colors:
    for y in objects:
        print(f"{x} {y}")



new_array = []
for x in colors:
    for y in objects:
        print(f"{x} {y}")
        new_array.append(f"{x} {y}")

print(new_array)



new_array_ = [f"{x} {y}" for x in colors for y in objects]
print(new_array_)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
flatten = [value for array in matrix for value in array]
print(flatten)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

numbers = [5, 10, 15]
labels = [f"{n} is even" if n % 2 == 0 else f"{n} is odd" for n in numbers]

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("""regla clave: 
        si poner if al final es para FILTRAR 

        [ x for x in iterable if something] => filtra los elementos 
        [ x if something else y  for value in  iterable ] => transforma los elementos 
        
        si poner if al inicio es para TRANSFORMAR 
        """)
numbers_ = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

numbe = [x for x in numbers_ if x%2 == 0]
print(numbe)

num = ["par" if x%2 == 0 else "impar" for x in numbers_]
print(num)

print("~~~~~~~~~~~~~~~~~Calling functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def square(n): return n**2
results = [square(x) for x in range(7)]
print(results)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
aa = [1,2,3,4]
bb = [11,22,33,44]
cc = [x+y for x,y in zip(aa,bb)]
print(cc)
print("~~~~~~~~~~~~~~~zip(aa,bb)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(zip(aa,bb))
print(list(zip(aa,bb)))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
xxx = [1,2,3,4,5,6]
yyy = [5,6,7,7,8]
print([ x[0] + x[1] for x in zip(xxx,yyy)])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")






















