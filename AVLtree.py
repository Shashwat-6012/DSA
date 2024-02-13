# AVL trees are self balancing Binary seacrh trees.
# On each inserstion of node, the Balanced check is done and if the tree is found 
# to be unbalanced then the tree is restructured for balancing it.

class AVL:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None
            self.height = 0
        
    root = None

    def Height(self, Node):
        if Node == None:
            return 0
        return Node.height
    
    def RightRotate(self, node):
        c = node.left
        t = c.right

        c.right = node
        node.left = t

        node.height = max(self.Height(node.left), self.Height(node.right)) + 1
        c.height = max(self.Height(c.left), self.Height(c.right)) + 1

        return c

    def LeftRotate(self, node): 
        c = node.right
        t = c.left

        c.left = node
        node.right = t
        node.height = max(self.Height(node.left), self.Height(node.right)) + 1
        c.height = max(self.Height(c.left), self.Height(c.right)) + 1

        return c
    
    def Rotate(self, node):
        left_height = self.Height(node.left)
        right_height = self.Height(node.right)
        if (left_height - right_height > 1):  # Unbalanced towards left
            if self.Height(node.left.left) >= self.Height(node.left.right):
                # This is the left left case
                return self.RightRotate(node)
            else:
                # This is the left right case
                node.left = self.LeftRotate(node.left)
                return self.RightRotate(node)
            
        elif (left_height - right_height < -1):  # Unbalanced towards right
            if self.Height(node.right.right) >= self.Height(node.right.left):
                # This is the right right case
                return self.LeftRotate(node)
            else:
                # This is the right left case
                node.right = self.RightRotate(node.right)
                return self.LeftRotate(node)

        return node
    
    
    def insertdrive(self, value, node):
        if node == None:
            Node = self.Node(value)
            return Node
        
        if value < node.value:
            node.left = self.insertdrive(value, node.left)
        
        elif value > node.value:
            node.right = self.insertdrive(value, node.right)

        node.height = max(self.Height(node.left), self.Height(node.right)) + 1

        return self.Rotate(node)

    
    def insert(self, value):
        if self.root == None:
            self.root = self.Node(value)
        else:
            self.insertdrive(value, self.root)
        
    def preorder(self, node):
        if node == None:
            return
        print(node.value, end = " ")
        self.preorder(node.left)
        self.preorder(node.right)

tree = AVL()

for i in range(6):
    tree.insert(i)

tree.preorder(tree.root)





