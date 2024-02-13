#Infix expression a + b
#Postfix expression ab+
from collections import deque
def convert(infix):
    stack = deque()
    postfix = ""
    
