# Segment trees contains queries and the ranges of a array. 

class Segmenttree:
    class Node:
        def __init__(self, startinterval, endinterval) -> None:
            self.data = 0
            self.startinterval = startinterval
            self.endinterval = endinterval
            self.left = None
            self.right = None


    def Constructtree(self, arr, start, end):
        if start == end:
            leaf = self.Node(start, end)
            leaf.data = arr[start]
            return leaf
        
        node = self.Node(start, end)
        mid = (start + end)//2
        node.left = self.Constructtree(arr, start, mid)
        node.right = self.Constructtree(arr, mid + 1, end)

        node.data = node.left.data + node.right.data
        return node


    def __init__(self, arr) -> None:
        self.arr = arr
        self.root = self.Constructtree(arr, 0, len(arr) - 1)

    def query(self, node, qsi, qei):   # THis is the query start index and query end index 
        # Query of a range, helper function.
        if node.startinterval >= qsi and node.endinterval <= qei:
            # Case 1 of query intervals. 
            return node.data
        
        if node.startinterval > qei or node.endinterval < qsi:
            # Case 2 of query interval
            return 0
        
        sum = self.query(node.left, qsi, qei) + self.query(node.right, qsi, qei)

        return sum 
    
    def update(self, node, index, value):
        if node.startinterval == node.endinterval == index:
            node.data = value
            return node
        
        elif node.startinterval <= index < node.endinterval:
            node.left = self.update(node.left, index, value)
            node.right = self.update(node.right, index, value)

        if node.left != None and node.right != None:
            node.data = node.left.data + node.right.data
        return node




arr = [3,8,7,6,-2,-8,4,9]
tree = Segmenttree(arr)

# sum = tree.query(tree.root, 1, 6)
# print(sum)
print(tree.root.data)
tree.update(tree.root, 2, 11)
print(tree.root.data)