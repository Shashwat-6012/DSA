# Questions on Linked List.
# Defining a proper Common List class for all the Questions.

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
    
def create_linked(elements):  # This function converts list to Linked list.
        root = None
        for i in elements:
            root = insert(root, i)
        return root

def create_list(root):   # This function converts Linked list to list.
     list = []
     ptr = root
     while ptr != None:
          list.append(ptr.data)
          ptr = ptr.next

     return list

def get(root, index):
     ptr = root
     for i in range(index):
          ptr = ptr.next
     return ptr

def print_linked(root):
    if root is None:
        print("Empty list")
    else:
        ptr = root
        while ptr != None: 
             print(ptr.data, end= " ")
             ptr = ptr.next

l1 = [1,2,3,4,5]
root = create_linked(l1)
# Q.1) Recursive Insertion in LinkedList at a given index.
print("Q.1) -->")
def RecursiveInsertion(root, item, index, ptr = root):
    if index == 1:
        temp1 = ptr.next
        temp = LinkedList(item)
        ptr.next = temp
        temp.next = temp1
        return root
    
    if index == 0:
         temp = LinkedList(item)
         temp2 = root
         temp.next = temp2
         root = temp
         return root
    return RecursiveInsertion(root, item, index-1, ptr.next)

newroot = RecursiveInsertion(root, 7, 3)
print_linked(newroot)
print()

# Q.2) Delete the duplicates for the given linked list.
print("Q.2) --> ")

def Rmvduplicates(root):
     l1 = create_list(root)
     l2 = list(set(l1))
     return create_linked(l2)

print_linked(root)
print()
print_linked(Rmvduplicates(root))
print()
# Q.3) Merge The two sorted lists
print("Q.3) -->")
def merger(root1,root2):
     ans = None
     ptr1 = root1
     ptr2 = root2
     while( ptr1 != None and ptr2 != None):
        if ptr1.data <= ptr2.data:
            ans = insert(ans, ptr1.data)
            ptr1 = ptr1.next
        else:
            ans = insert(ans, ptr2.data)
            ptr2 = ptr2.next

        
     while(ptr1 != None):
          ans = insert(ans, ptr1.data)
          ptr1 = ptr1.next
     
     while(ptr2 != None):
          ans = insert(ans, ptr2.data)
          ptr2 = ptr2.next

     return ans

l2 = [1, 3, 5, 20]
l3 = [1,2,9,14]
root1 = create_linked(l2)
root2 = create_linked(l3)
print_linked(merger(root1, root2))
print()

#Q.4) Cycle detection in Linked List.
print('Q.4) -->')
def Cycle(root):
     fptr = root
     sptr = root
     while(fptr != None and fptr.next != None):
          fptr = fptr.next.next
          sptr = sptr.next
          if fptr == sptr:
               return True
     return False

#Creating a Cycled Linked List.
node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)
node6 = LinkedList(6)
node7 = LinkedList(7)
node8 = LinkedList(8)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
# node8.next = node3


print(Cycle(node1))

# Q.5) length of the cycle.
# Once you found the slow and faster pointers equal position. i.e the cycle is found, start
# moving the slow pointer again till it reaches the faster pointer ans count the number of counters 
# count will give the length of the cycle.
print("Q.5) -->")
def lencycle(root):
     fptr = root
     sptr = root
     flag = 0
     while(fptr != None and fptr.next != None):
          fptr = fptr.next.next
          sptr = sptr.next
          if fptr == sptr:
               flag = 1
               break
     if flag == 0:
          return 0
     count = 1
     sptr = sptr.next
     while sptr != fptr:
          sptr = sptr.next
          count += 1
     return count

print(lencycle(node1))

# Q.6) Find the starting point of the cycle.
print("Q.6) -->")
def startpos(root):
    l = lencycle(root)
    if l == 0:
         return
    first = root
    second = root
    for i in range(l):
         second = second.next
    
    while first != second:
         first = first.next 
         second = second.next

    return first

if startpos(node1) != None:
     print(startpos(node1).data)
else:
     print("No cycle present.")
          
# Q.7) Happy number question, leetcode.
print("Q.7) -->")

def findsqaure(num):
     ans = 0
     while (num > 0):
          rem = num%10
          ans += rem*rem
          num = num//10
     return ans

def isHappy(num):
     slow = num
     fast = num
     slow = findsqaure(slow)
     fast = findsqaure(findsqaure(fast))
     while slow != fast:
          slow = findsqaure(slow)
          fast = findsqaure(findsqaure(fast))
          if slow == 1 or fast == 1:
               return True
     
     return False

print(isHappy(12))

# Q.8) Middle element of the Linked list, with only a single pass. (Without finding the length.)
print("Q.8) -->")
l1 = [1,2,3,4,5,6]
root = create_linked(l1)
def Middle(root):
     slow = root
     fast = root
     while(fast != None and fast.next != None):
          fast = fast.next.next
          slow = slow.next
     
     return slow

print(Middle(root).data)

# Q.9) Merge sort of linked list.
# Will be using the Functions Merger and Middle element for merging the two lists
# and finding the middle element.
print("Q.9) -->")
# Driver function for the length of the list.
def length(root):
     ptr = root
     l = 0
     while ptr != None:
          ptr = ptr.next
          l += 1
     return l

def Mergesort(root):
     mid = Middle(root)
     if root is None or root.next is None:
          return root
     
     left = Mergesort(root)
     right = Mergesort(mid)

     return merger(left, right)

# l1 = [1,6,5,3,4,2]
# root = create_linked(l1)
# print_linked(Mergesort(root))


# Q.10) Bubble sort, using recursion.
print("Q.10) -->")

def Bubble(root, r, c = 0):
     if r == 0:
          return root
     else:
          if c < r:
               first = get(root, c)
               second = get(root, c + 1)
               if first.data > second.data:
                    # Perform the swaps. 
                    # Three cases.
                    if first == root:
                         root = second
                         first.next = second.next
                         second.next = first
                    
                    elif second.next == None:
                         prev = get(root, c - 1)
                         prev.next = second
                         first.next = None
                         second.next = first
                    else:
                         prev = get(root, c - 1)
                         prev.next = second
                         first.next = second.next
                         second.next = first
               return Bubble(root, r, c + 1)
          return Bubble(root, r - 1)
l1 = [1,6,5,3,4,2]
root = create_linked(l1)
l = length(root)
newr = Bubble(root, l-1)
print_linked(newr)
print()


# Defining a new class of Linkedlist
class LinkedList():
     def __init__(self, head) -> None:
          self.head = head
          ptr = head
          while (ptr.next != None):
               ptr = ptr.next
          self.tail = ptr

class Node():
     def __init__(self, data) -> None:
          self.data = data
          self.next = None

def insert(root, node):
        temp = Node(node)
        if root == None:
            root = temp
        else:
            ptr = root
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = temp
        return root
    
def create_linked(elements):  # This function converts list to Linked list.
        root = None
        for i in elements:
            root = insert(root, i)
        linkedlist = LinkedList(root)
        return linkedlist

def get(Linkedlist, index):
     ptr = Linkedlist.head
     for i in range(index):
          ptr = ptr.next
     return ptr

def print_linked(linkedlist):
    root = linkedlist.head
    if  root is None:
        print("Empty list")
    else:
        ptr = root
        while ptr != None: 
             print(ptr.data, end= " ")
             ptr = ptr.next

# Q.11) Reversing the Linked List using Recursion.
print("Q.11) -->")

def Reverse(l1, node):
     if node == l1.tail:
          l1.head = l1.tail
          return
     Reverse(l1, node.next)
     l1.tail.next = node
     l1.tail = node
     l1.tail.next = None

l1 = [1,2,3,4,5]
ll1 = create_linked(l1)
Reverse(ll1, ll1.head)
print_linked(ll1)
print()
# Q.12) Reversing the list without recursion.
print("Q.12) -->")
def Reversewithoutrecurse(linkedlist):
     prev = None
     present = linkedlist.head
     nxt = present.next
     while present != None:
          present.next = prev
          prev = present
          present = nxt
          if nxt != None:
               nxt = nxt.next
          
     linkedlist.head = prev
     return linkedlist

l1 = [6,5,4,3,2,1,0]
ll1 = create_linked(l1)
Reversewithoutrecurse(ll1)
print_linked(ll1)
print()
# Q.13) Reverse a part of the Linkedlist.
print("Q.13) -->")
def Reversepart(linkedlist, left, right):
     prev = None
     present = linkedlist.head
     nxt = present.next
     counter = 1
     while counter != right + 1:
          if counter == left - 1:
               ptr = present
               for _ in range(right - counter):
                    ptr = ptr.next
               present.next = ptr
               prev = present
               present = nxt
               if nxt != None:
                    nxt = nxt.next
          elif counter == left:
               ptr = present
               for _ in range(right + 1 - counter):
                    ptr = ptr.next
               present.next = ptr
               prev = present
               present = nxt
               if nxt != None:
                    nxt = nxt.next
          elif left < counter <= right:
               present.next = prev
               prev = present
               present = nxt
               if nxt != None:
                    nxt = nxt.next
          counter += 1
          # in case left is 1 then head will change.
     if left == 1:
          linkedlist.head = get(linkedlist, right-1)
     return linkedlist
          
l1 = [1,2,3,4,5,6,7]
ll1 = create_linked(l1)
Reversepart(ll1, 2, 5)
print_linked(ll1)
print()
# Q.14) Reorder the List.
# THe order is if:  1 --> 2 --> 3 --> 4 --> 5
# the reorder list will be:  1 --> 5 --> 2 --> 4 --> 3
print("Q.14) --> ")

def Reorder(Linkedlist):
     len = length(Linkedlist.head)
     start = 0
     end = len - 1
     temp = get(Linkedlist, start)
     if len%2 == 0:
          while start != end+1:
               st = Node(get(Linkedlist, start).data)
               # print(st.data)
               if start == 0:
                    root = st
               if start != 0:
                    temp.next = st
               en = Node(get(Linkedlist, end).data)
               print(en.data)
               st.next = en
               temp = en
               start += 1
               end -= 1
     else:
          while start != end:
               st = Node(get(Linkedlist, start).data)
               # print(st.data)
               if start == 0:
                    root = st
               if start != 0:
                    temp.next = st
               en = Node(get(Linkedlist, end).data)
               print(en.data)
               st.next = en
               temp = en
               start += 1
               end -= 1
          finalnode = Node(get(Linkedlist, start).data)
          print(finalnode.data)
          en.next = finalnode
     newll = LinkedList(root)
     return newll

l1 = [1,2,3,4,5,6,7,8,9]
ll1 = create_linked(l1)
newll = Reorder(ll1)
print_linked(newll)
print()









               
     
     