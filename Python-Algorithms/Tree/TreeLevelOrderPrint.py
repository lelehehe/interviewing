from Tree import Node
import collections

#http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Trees/Trees%20Interview%20Problems%20-%20SOLUTIONS/Tree%20Level%20Order%20Print%20-%20SOLUTION.ipynb

def levelOrderPrint(tree):
    q = collections.deque()
    q.append(tree)
    currentCounter, nextCount = 1, 0

    while len(q):
        item = q.popleft()
        currentCounter -= 1
        print(item.val, end=" ")
        if item.left:
            q.append(item.left)
            nextCount += 1
        if item.right: 
            q.append(item.right)
            nextCount += 1
        if currentCounter == 0:
            print()
            currentCounter = nextCount
            nextCount = 0


if __name__ == "__main__":
    tree = Node(1)

    t2 = Node(2)
    t2.left = Node(4)
    t3 = Node(3)
    t3.left = Node(5)
    t3.right = Node(6)
    tree.left = t2
    tree.right = t3

    levelOrderPrint(tree)
    #result should be: 
    #1
    #2 3
    #4 5 6
