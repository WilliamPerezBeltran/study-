
class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None 

class SinglyLinkedList():
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

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next 
        print("None")
    
    def is_empty(self):
        return self.head == None




lista = SinglyLinkedList()
lista.insert_at_beginning(3)
lista.insert_at_beginning(2)
lista.insert_at_beginning(1)
lista.insert_at_end(4)
lista.traverse()
print(lista.is_empty())


lista1 = SinglyLinkedList()
print(lista1.is_empty())
