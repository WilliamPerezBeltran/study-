# ~~~~~~~~~~ mutation ~~~~~~~~~~
"""
mutation means changing an object in place without creating a new one 
mutacion significa cambiar un object en su lugar sin crear uno nuevo 
"""
lst = [1,2,3]
print(lst) # => [1,2,3]
lst.append(4)
print(lst) # => [1,2,3,4]


# ~~~~~~~~~~ Aliasing ~~~~~~~~~~

"""
Aliasing happens when two variables reference the same object in memory.
Alias pasa cuando dos variables referencian the mismo objecto en memoria.
"""

a = [1,2,3]
print(a) # => [1,2,3]
b = a
b.append(4)
print(a) # => [1,2,3,4]

# ~~~~~~~~~~ mutation ~~~~~~~~~~
"""
Cloning creates a copy of the object so changes don't affect the original .
Clonar crea una copoia del object por lo tanto los cambios no afectan el objecto original. 
"""

import copy
# primer forma con [:]
a = [10,20,30]
b = a[:]
b.append(40)
print(a) # => [10,20,30]
print(b) # => [10,20,30,40]

# segunda forma con copy.deepcopy(objc)
nested_a = [[2,2],[3,3],[4,4]]
nested_b = copy.deepcopy(nested_a)
nested_b[0].append(99)
print(nested_a)  # => [[2,2],[3,3],[4,4]]
