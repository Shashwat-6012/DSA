# Q.1) implement Queue using a stack.

class Queue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []
    
    def push(self, element):
        self.stack1.append(element)
    
    def pop(self):
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return ans
    
    def display(self):
        print(self.stack1)
    
Q = Queue()
Q.push(1)
Q.push(2)
Q.push(3)
Q.push(4)
Q.display()
print(Q.pop())
print(Q.pop())
Q.display()

# Q.2) Hackerrank Game of two stacks.
print("Q.2) -->")
def Game(stack1, stack2, maxtotal, count = 0, total = 0):
    if total >= maxtotal:
        return count
    
    if len(stack1) == 0 or len(stack2) == 0:
        return count

    count1 = Game(stack1[:-1], stack2, count + 1, total + stack1[-1])
    count2 = Game(stack1, stack2[:-1], count + 1, total + stack2[-1])

    return max(count1, count2)

a = [1,6,4,2,4]
b = [5,8,1,2]
maxsum = 10
print(Game(a,b,maxsum) - 1)

# Q.3) Paranthesis checker.
print("Q.3) -->")

def Paranthesis(str):
    para = ['(', '{', '[']
    stack = []
    for i in str:
        if i in para:
            stack.append(i)
        if i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()

    print(stack)
    if stack:
        return False
    else:
        return True

print(Paranthesis("[]{}()"))
