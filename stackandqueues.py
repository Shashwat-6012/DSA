# Stacks can be implemented by lists as well as deque.
# deque from collections hsa a builtin parameter maxlen to address the max len of the stack.

from collections import deque

stack = deque(maxlen=5)

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)

print(stack)

stack.pop()
print(stack)
stack.append(4)
print(stack)
print(stack[0])
