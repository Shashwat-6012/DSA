# Q.1) Print 1 to n numbers in recursion function.
print("Q.1)")
def numberprint(n, flag = 0):
    if n == 0:
        return
    else:
        flag = 1 + flag
        print(flag, end = " ")
        numberprint(n-1, flag)

numberprint(5)
print()
# Q.2) Factorial of a number. 
print("Q.2) ")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

# Q.3) Sum of digits in a number
print("Q.3) ")

def Sumdigit(n):
    if n == 0:
        return ' '
    else:
        return   str(n%10) + str(Sumdigit(n//10))
    
print(Sumdigit(1356))

# Q.4) Count the number of steps to make a number zero. 
# if the number is even divide it by 2, else substart it by 1
print("Q.4) ")
def countsteps(n, steps = 0):
    if n == 0:
        return steps
    else:
        steps += 1
        if n%2 == 0:
            return countsteps(n//2, steps)
        else:
            return countsteps(n-1, steps)

print(countsteps(8))
            
# Q.5) Check whether the array is sorted or not. 
print("Q.5) ")
def is_sorted(arr, i = 0):
    temp = arr
    if i == len(temp) - 1:
        return True
    if temp[i] < temp[i+1] and is_sorted(temp, i+1):
        return True
    else:
        return False

arr = [1 , 2, 3, 4, 7, 10, 11]
print(is_sorted(arr))

# Q.6) Linear search for suplicate elements in an array.
print("Q.6) ")
def recursive_linear(arr, ele, i = 0, pos = []):
    newpos = pos
    if arr[i] == ele:
        newpos.append(i)
    if i == len(arr) - 1:
        return newpos
    i += 1
    return recursive_linear(arr, ele, i, newpos)
    
arr = [1,3,4,5,5,6,7,8]
print(recursive_linear(arr, 5))

# Q.7) Print a traingle of n rows and n colunms. 
# eg:   * * * * 
#       * * *
#       * *
#       *                 n = 4

print("Q.7) ")

def traingle(r, c = 0):
    if r == 0:
        return
    
    if c < r:
        traingle(r, c+1)
        print("* ", end = "")
    else:
        traingle(r-1)
        print()

traingle(4)