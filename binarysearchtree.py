def find_min(root):
    p = root
    while True:
        if p.left is None:
            return p
        else:
            p = p.left
    
def find_max(root):
    p = root
    while True:
        if p.right is None:
            return p
        else:
            p = p.right



class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            max_val = find_max(self.left)
            self.data = max_val.data
            self.left = self.left.delete(max_val.data)

        return self

def create_tree(ele):
        root = TreeNode(ele[0])
        for i in range(1, len(ele)):
            root.add_child(ele[i])

        return root 


def print_tree(root):
    ele = []
    if root is None:
        return None
    
    print_tree(root.left)

    print(root.data, end = " ")

    print_tree(root.right)


def search(root, val):
    if val == root.data:
        return True
    
    if val < root.data:
            if root.left:
                search(root.left, val)
            else:
                return False
            
    if val > root.data:
            if root.right:
                search(root.right, val)
            else:
                return False




        

    

ele = [17, 4, 1, 20, 9, 23, 18, 34]

root = create_tree(ele)

print_tree(root)
print()

root.delete(9)

print_tree(root)
print()
# min = find_min(root)
# print(min.data)

# max = find_max(root)
# print(max.data)
# print("????")

