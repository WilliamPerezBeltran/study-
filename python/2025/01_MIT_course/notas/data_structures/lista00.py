class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 


class lista():
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
        current = new_node
        while current:
            current = current.next 
               
        current = new_node 

    def traverse(self):
        current = self.head
        while current: 
            print(current.data, end=" -> ")
            current = current.next


a = lista()
a.insert_at_beginning(1)
a.insert_at_beginning(2)
a.insert_at_beginning(3)
a.insert_at_end(4)
a.traverse()
print("======")
a.insert_at_end(5)
a.traverse()


