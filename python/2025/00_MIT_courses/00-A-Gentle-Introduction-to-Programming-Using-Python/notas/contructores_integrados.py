# ~~~~~~~ Listas ( llist ) ~~~~~~~

#literal 
lista = [1,2,3]
# Contructor 
lista = list((1,2,3)) # => [1,2,3]
lista = list("abc") # => ["a","b","c"]
lista = list() # => [] 

# ~~~~~~~ Tuples ( tuple ) ~~~~~~~

#literal 
tuplas = (1,2,3)
# Contructor 
tuplas = tuple([1,2,3])
tuplas = tuple("abc")
tuplas = () or tuple()
tuplas = ()


# ~~~~~~~ Conjuntos ( set ) ~~~~~~~

#literal 
lista = [1,2,3]
# Contructor 
conjunto = {1,2,3}
conjunto = set([1,2,3])
conjunto = set()

# ~~~~~~~ Diccionarios ( dict ) ~~~~~~~

#literal 
dic = {"a": 1, "b": 2}
# Contructor 
dic = dict(a=1,b=2)
dic = dict([("a",1),("b",1)])
dic = dict()

# ~~~~~~~ Rango (range) ~~~~~~~

# no tiene literal solo contructor 
# Contructor 
r = range(5)
r = range(1,10,1)
