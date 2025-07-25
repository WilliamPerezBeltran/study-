from os import system

system("clear")
from pilas import Pila

pila =  Pila(6)

pila.push(26)
pila.push(23)
pila.push(2635)
pila.push(2237)
pila.push(17)

pila.verTope()
pila.show()
pila.pop()
pila.pop()
print("-------")
pila.show()
pila.verTope()

print(pila.top())

