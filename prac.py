class BST:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None
            self.height = 0
    
    root = None

    def Height(self, node):
        if node == None:
            return 0
        else:
            return node.height
        
    def LeftRotate(self, node):
        c = node.right
        t = c.left

        c.left = node
        node.right = t
        node.height = max(self.Height(node.left), self.Height(node.right)) + 1
        c.height = max(self.Height(c.left), self.Height(c.right)) + 1

        return c

    def RightRotate(self, node):
        c = node.left
        t = c.right

        c.right = node
        node.left = t

        node.height = max(self.Height(node.left), self.Height(node.right)) + 1
        c.height = max(self.Height(c.left), self.Height(c.right)) + 1

        return c

    def Rotate(self, node):
        left_height = self.Height(node.left)
        right_height = self.Height(node.right)
        if left_height - right_height > 1: # Unbalanced towards left
            if self.Height(node.left.left) - self.Height(node.left.right) > 0:
                # left left case
                return self.RightRotate(node)
            else:
                #left right case
                node.left = self.LeftRotate(node.left)
                return self.RightRotate(node)
        elif left_height - right_height < -1: # Unbalanced towards right
            if self.Height(node.right.left) - self.Height(node.right.right) < 0:
                # right right case
                return self.LeftRotate(node)
            else:
                # right left case
                node.right = self.RightRotate(node.right)
                return self.LeftRotate(node)
        
        return node



    def insertdrive(self, node, value):
        if node == None:
            Node = self.Node(value)
            return Node
        if value > node.value:
            node.right = self.insertdrive(node.right, value)
        elif value < node.value:
            node.left = self.insertdrive(node.left, value)
        
        node.height = max(self.Height(node.left), self.Height(node.right)) + 1

        return self.Rotate(node)
    
    def insert(self, value):
        if self.root == None:
            self.root = self.Node(value)
        else:
            self.insertdrive(self.root, value)
        
    
tree = BST()
for i in range(1000):
    tree.insert(i)

print(tree.root.height)
