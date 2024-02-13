# find the min number in an array using Linear seacrh

def findmin(arr):
    min_no = arr[0]
    for i in range(1,len(arr)):
        min_no = min(arr[i], min_no)
    return min_no

# arr = [18, 23, 10, 13, 5, 17]
# minno = findmin(arr)
# print(minno)

# Calculate How many number contains even digits like 24 contains 2 digits hence even number of digits.

def findeve(arr):
    number = 0
    for i in arr:
        digit = len(str(i))
        if digit%2 == 0:
            number += 1
        else:
            continue
    
    return number

arr = [12, 3456, 2, 6, 7896]

no = findeve(arr)
# print(no)

# Linear search using recursion. 

def recursive_linear(arr, ele, i = 0):
    if arr[i] == ele:
        return True
    elif i == len(arr) - 1:
        return False
    else:
        i += 1
        return recursive_linear(arr, ele, i)
    
arr = [1,2,3,4,5,6,7,10]

print(recursive_linear(arr, 10))