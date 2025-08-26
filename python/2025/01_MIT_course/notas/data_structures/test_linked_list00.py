import unittest 
from linked_list00 import (
        Node, 
        SinglyLinkedList
    )

class TestLinkedList00(unittest.TestCase):
    def test_empty(self):
        my_lista = SinglyLinkedList()
        self.assertEqual(my_lista.is_empty(),True)

    def test_no_empty(self):
        lista = SinglyLinkedList()
        lista.insert_at_beginning(1)
        self.assertEqual(lista.is_empty(), False)
    
     


if __name__ == "__main__":
    unittest.main()




