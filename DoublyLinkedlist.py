class Node():
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinked():
    def __init__(self) -> None:
        self.head = None
        self.lastNode = None
    
    def insert(self, item):
        temp = Node(item)

        if self.lastNode == None and self.head is None:
            self.head = temp
            self.lastNode = self.head
        else:
            self.lastNode.next = temp
            temp.prev = self.lastNode