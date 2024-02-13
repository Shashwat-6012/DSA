# New way of Binary seacrh tree.
class BST:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None
            self.height = 0
    
    # def __init__(self, rootval) -> None:  || You can do a constructor for the root value.
    #     self.root = self.Node(rootval)
    root = None

    def Height(self, Node):
        if Node == None:
            return 0
        h = max(self.Height(Node.left), self.Height(Node.right))
        return h + 1
    
    def insertdrive(self, data, node):
        if node == None:
            Node = self.Node(data)
            return Node
        
        if data < node.value:
            node.left = self.insertdrive(data, node.left)
        
        if data > node.value:
            node.right = self.insertdrive(data, node.right)
        
        node.height = max(self.Height(node.left), self.Height(node.right))
        return node
    
    def insert(self, value):
        if self.root == None:
            self.root = self.Node(value)
        else:
            self.insertdrive(value, self.root)
    
    def Balanced(self, node):
        if node == None:
            return True
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        if (abs(left_height - right_height) <= 1):
            return (self.Balanced(node.left) and self.Balanced(node.right))
        else:
            return False
    
    def preorder(self, root):
        if root == None:
            return
        print(root.value, end = " ")
        self.preorder(root.left)
        self.preorder(root.right)

    def Inorder(self, root):
        if root == None:
            return
        
        self.Inorder(root.left)
        print(root.value, end = " ")
        self.Inorder(root.right)
    
    def postorder(self, root):
        if root == None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end = " ")

    def displaydriver(self, node, lvl = 0):
        if node == None:
            return
        print(lvl*("--" if lvl > 0 else "    ") + str(node.value))
        self.displaydriver(node.left, lvl + 1)
        self.displaydriver(node.right, lvl + 1)

    def display(self):
        if self.root is None:
            return "Empty"
        else:
            self.displaydriver(self.root)

    
    # def insert(self, data, node):   This driver code needs a better Height update algo.
    #     if data < node.value:
    #         if node.left == None:
    #             node.left = self.Node(data)
    #             return
    #         else:
    #             self.insert(data, node.left)
    #             node.height = max(self.Height(node.left), self.Height(node.right))
        
    #     if data > node.value:
    #         if node.right == None:
    #             node.right = self.Node(data)
    #             return
    #         else:
    #             self.insert(data, node.right)
    #             node.height = max(self.Height(node.left), self.Height(node.right))

def populate(nums):
    tree = BST()
    for i in nums:
        tree.insert(i)
    return tree

def populatedriver(tree, nums, start, end):
    if start > end:
        return
    
    mid = (start + end)//2
    tree.insert(nums[mid])
    populatedriver(tree, nums, start, mid - 1)
    populatedriver(tree, nums, mid + 1, end)

def populatesorted(nums):
    tree = BST()
    populatedriver(tree, nums, 0, len(nums)-1)
    return tree

def heightdisplay(root):
    if root == None:
        return
    print(f"Height of node {root.value}: " + str(root.height))
    heightdisplay(root.left)
    heightdisplay(root.right)

# tree = BST(15)
# tree.insert(20, tree.root)
# tree.insert(11, tree.root)
# tree.insert(9, tree.root)
# tree.insert(13, tree.root)
# tree.insert(17, tree.root)
# tree.insert(12, tree.root)
# tree.insert(25, tree.root)
# tree.insert(23, tree.root)
# tree.insert(21, tree.root)


nums = [5,2,7,1,4,6,9,8,3,10] # This is a balanced tree.
# tree = populate(nums)

# nums = [20, 19, 8, 15, 2, 13, 1] This is an unbalanced tree.
# tree = populatesorted(nums)
tree = populate(nums)

tree.display()