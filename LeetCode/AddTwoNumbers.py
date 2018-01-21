#https://leetcode.com/problems/add-two-numbers/description/


import os
import sys
cwd = os.getcwd()
print(cwd)
sys.path.append(cwd + '/lib/')
from LinkedList import LinkedList, Node

l = LinkedList([2, 3, 4])


def add_two_number(l1, l2):
    pass

def test_add_two_number():
    stubs = [test_add_two_number]
    for stub in stubs:    
        assert stub('[](){([[[]]])}(') == False


