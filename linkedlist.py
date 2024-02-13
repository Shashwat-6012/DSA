class LinkedList():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def insert(root, node):
        temp = LinkedList(node)
        if root == None:
            root = temp
        else:
            ptr = root
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = temp
        return root
    
def create_linked(elements):
        root = None
        for i in elements:
            root = insert(root, i)
        return root


def print_linked(root):
    if root is None:
        print("Empty list")
    else:
        ptr = root
        while ptr != None: 
             print(ptr.data, end= " ")
             ptr = ptr.next

def delete(root, item):
    if root is None:
          print("Linked list empty")
    else:
        ptr = root
        flag = 0
        while ptr != None:
             if ptr.data == item:
                  flag = 1
             ptr = ptr.next
        if flag == 1:
            ptr = root
            while ptr.next.data != item:
                ptr = ptr.next
            
            ptr.next = ptr.next.next
            return root 
        else:
             print("item not present in List")
    
l1 = [1,2,3,4,5]
root = create_linked(l1)
print_linked(root)
print()
newroot = delete(root, 4)
print_linked(newroot)


