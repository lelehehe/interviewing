# Problem
# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
# You've been given the Linked List Node class 

import os
import sys
cwd = os.getcwd()
print(cwd)
sys.path.append(cwd + '/lib/')
from LinkedList import LinkedList, Node

l = LinkedList([2, 3, 4])

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def has_cycle(node):
    travel1 = node
    travel2 = node
    while travel1 != None and travel2.nextnode != None:
        travel1 = travel1.nextnode
        travel2 = travel2.nextnode.nextnode
        if travel1 == travel2:
            return True
    return False
#endregion

def test_fcycle_check():
    # CREATE CYCLE LIST
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a # Cycle Here!

    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z


    stubs = [has_cycle]
    for stub in stubs:    
        assert stub(a) == True
        assert stub(x) == False
