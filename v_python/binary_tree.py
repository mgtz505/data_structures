###Implementation of a Binary Tree

class Node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
    
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

### Test Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.left.right = Node(6)
print("In-order traversal of binary tree:")
print(inOrder(root))