class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None 

class lista():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node 
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self,data):
        # verificar si la lista está vacía 
        assert self.head is not None , "lista vacia, no hay nada que borrar " 
       # Revisar si el noddo a borrar es els primero  
        if self.head.data == data:
            self.head = self.head.next 
            return 

        # Recorrer la lista buscando el nodo a borrar 
        current = self.head
        while current:
            if current.next and current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next 

        # caso especial: nodo no encontrado 
        return False
        

    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

l = lista()
l.insert_at_beginning(2)
l.insert_at_beginning(1)
l.insert_at_end(40)
# 1 2 40
l.traverse()
l.delete(1)
l.traverse()









