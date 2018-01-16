# Problem Statement:
# The key insight is that a stack reverses order (while a queue doesn't). A sequence of elements pushed on a stack comes back in reversed order 
# when popped. Consequently, two stacks chained together will return elements in the same order, since reversed order reversed again is original order.
# We use an in-stack that we fill when an element is enqueued and the dequeue operation takes elements from an out-stack. 
# If the out-stack is empty we pop all elements from the in-stack and push them onto the out-stack.


#region my implementation
# ============= Note ========
# ...
class Queue2Stacks(object):
    def __init__(self):
        pass
#endregion

def test_foo():
    q = Queue2Stacks()
    
    for i in xrange(5):
        q.enqueue(i)
        
    for i in xrange(5):
        print q.dequeue()
