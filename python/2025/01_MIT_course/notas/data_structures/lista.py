"""

Nodo actual: A -> None 
current = A 

Nodo nuevo: B -> None 
new_node = B

Conecto A con B 
current.next = new_node 

Ahora la lista es: A -> B -> None

"""



class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 

    def insert_at_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node 
            return 
        current = self.head
        
        while current.next:
            current = current.next  

        current.next = new_node 

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" => ")
            current = current.next 
        print("none")

lista = SinglyLinkedList()
lista.insert_at_beginning(1) 
lista.insert_at_end(2) 
lista.display() 

print("====")
lista = SinglyLinkedList()
lista.insert_at_beginning(1) 
lista.insert_at_end(2) 
lista.insert_at_end(3) 
lista.insert_at_end(4) 
lista.insert_at_end(5) 
lista.insert_at_end(6) 
lista.display() 

# class Node_():
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
# 
# class Lista():
#     def __init__(self):
#         self.head = None 
#     def at_beginning(self,data):
#     def at_end(self,data):
#     def show(self):
# 
# class Lista():
#     def __init__(self):
#         self.head = None 
#     def at_beginning(self,data):
#     def at_end(self,data):
#     def show(self):
# 
# class Lista():
#     def __init__(self):
#         self.head = None 
#     def at_beginning(self,data):
#     def at_end(self,data):
#     def show(self):
# 
# class Lista():
#     def __init__(self):
#         self.head = None 
#     def at_beginning(self,data):
#     def at_end(self,data):
#     def show(self):
# 
# class Lista():
#     def __init__(self):
#         self.head = None 
#     def at_beginning(self,data):
#     def at_end(self,data):
#     def show(self):

class Lista():
    def __init__(self):
        self.head = None 
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
        pass
    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        if not current:
            self.head = new_node 
            return 
        while current.next:
            current = current.next
        current.next = new_node  

    def insert_after(self, prev_node, data):
        pass
    def delete_node(self, key):
        pass
    def search(self, key):
        pass
    def traverse(self, ):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next 
        print("None")

        pass
    def is_empty(self, ):
        pass
    def get_length(self, ):
        pass


a = Lista()
a.insert_at_beginning(1)
a.insert_at_beginning(2)
a.insert_at_beginning(3)
a.insert_at_end(4)
a.traverse()












