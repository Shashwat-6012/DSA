# This is a paranthesis matching problem using stack.
from collections import deque

def paranthesis_check(str):
    stack = deque()
    for i in str:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False 

ps = str(input("Please enter the string to be checked: "))
check = paranthesis_check(ps)
print("The given string has balanced paranthesis" if check else "The given string has unbalanced paranthesis")


