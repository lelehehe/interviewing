class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
   
class LinkedList(object):
    def __init__(self, values):
        self.head = None
        if len(values) != 0:
            for value in values[::-1]:  # same as reversed(values)
                node = Node(value)
                node.nextnode = self.head
                self.head = node
        
    def print(self):
        p = self.head
        while p != None: 
            print(p.value)
            p = p.nextnode
        
list = LinkedList([2,3,4])
list.print()



