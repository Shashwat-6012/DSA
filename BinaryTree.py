class Binarytree:
    class Node:
        def __init__(self, value) -> None:
            self.data = value
            self.left = None
            self.right = None
    
    root = None

    def populate(self, node):
        left = input(f"Do you want to insert left of {node.data}: (yes/no) ")
        if left == "yes":
            nodeval = int(input(f"Please enter the left {node.data} node value: "))
            node.left = self.Node(nodeval)
            self.populate(node.left)
        
        right = input(f"Do you want to insert right of {node.data}: (yes/no) ")
        if right == "yes":
            nodeval = int(input(f"Please enter the right {node.data} node value: "))
            node.right = self.Node(nodeval)
            self.populate(node.right)


    def CreateBinary(self):
        rootval = input("Please Enter the root value: ")
        self.root = self.Node(rootval)
        self.populate(self.root)

    def display(self, node, indent = " "):
        if node == None:
            return
        print(indent + str(node.data))
        self.display(node.left, indent + "--")
        self.display(node.right, indent + "--")

tree = Binarytree()
tree.CreateBinary()
tree.display(tree.root)
        
