class Node():
    def __init__(self,data,next):
       self.data = data 
       self.next = next  

def traverse(node):
    while node != None:
        print(node)
        print(node.data)
        node = node.next



node1 = Node(1,None)
node2 = Node(2,node1)
node3 = Node(3,node2)
node4 = Node(4,node3)

traverse(node4)
