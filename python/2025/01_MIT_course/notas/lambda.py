
from functools import reduce 

"""
 lambda es una funcion anonima que no requiere de identificador para ser invocado 
Tiene las mismas caraceristicas que tiene una funcion definida es decir se puede 
pasar como parametro, retornar en fucniones, pero a diferencia de def solo se puede utilizar 
en una sola linea. 
    * sintaxis:

    lambda argmentos: expressions 

"""

def add(a,b):
    return a+b 
print(add(2,3))

suma = lambda a,b:a+b 
print(suma(2,3))

doblar = lambda x: x*2
print(doblar(34))

resultado = map(lambda x:x*2,[1,2,3,4,5,6,7] )  #Devuelve un objeto map (iterador).
print(list(resultado))  # Si lo quieres como lista, debes envolverlo en list().

resultado = filter(lambda x: x>0, [-5,-4,-3,-2,-1,0,1,2,3,4,5,6])
print(list(resultado))

suma = reduce(lambda a,b: a+b, [-5,-4,-3,-2,-1,0,1,2,3,4,5,6])
print(suma)



