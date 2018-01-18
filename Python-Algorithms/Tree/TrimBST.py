from Tree import Node
from TreeLevelOrderPrint import levelOrderPrint
import collections

# refer to TrimBST.png
def trimBST(tree, minVal, maxVal):
    if not tree:
        return tree

    if tree.val < minVal:
        tree = trimBST(tree.right, minVal, maxVal)
    elif tree.val > maxVal:
        tree = trimBST(tree.left, minVal, maxVal)
    else:
        tree.left = trimBST(tree.left, minVal, maxVal)
        tree.right = trimBST(tree.right, minVal, maxVal)
    return tree


tree = Node(8)
t6 = Node(6)
t6.left = Node(4)
t6.right = Node(7)
t3 = Node(3)
t3.left = Node(1)
t3.right = t6
t14 = Node(14)
t14.left = Node(13)
t10 = Node(10)
t10.right = t14
tree.left = t3
tree.right = t10

levelOrderPrint(tree)
trimBST(tree, 5, 13)
levelOrderPrint(tree)

#2nd result should be: 
#     8
# 6      10
#   7       13
