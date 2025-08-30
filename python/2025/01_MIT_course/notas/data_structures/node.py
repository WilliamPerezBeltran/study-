class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 

nodo1 = Node(1)
nodo2 = Node(2)
nodo3 = Node(3)
nodo4 = Node(4)

nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4

nodo_actual = nodo1
while nodo_actual:
    print(nodo_actual.data)
    nodo_actual = nodo_actual.next
