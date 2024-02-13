# Most type of questions in Binary search.

# Q.1) Ceiling of a target number of an array (Given)
# Ceiling of a number in array is the smallest number that is greater than or equal to the target. 
# for eg arr = [1,4,5,6,7,10], target = 5, the ceiling of target 5 in arr will be 6

def Ceilingsearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]
    return arr[start]


# Q.2) Floor of the number in an array is the exact opposite of the above problem.
# The largest element in the array less than or equal to the target. 
print("Q.2) Answer --> ")
def Floorsearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]
    return arr[end]       # At this point the start pointer is one ahend of the end ...
#... pointer (While loop condition breaks)

arr = [2,3,5,9,14,16,18]
target = 9
ans = Floorsearch(arr, target)
print(ans)

# Q.4) Find the start and the end positons of a target value in an array. 
# eg. arr = [1 , 3 , 3, 3, 4 ,7, 9] target = 3 and ans = [1,3]

print("Q4.) Answer --> ")
def Search(arr, target, findstart):
    ans = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if target < arr[mid]:
            end = mid-1
        elif target > arr[mid]:
            start = mid + 1
        else:
            ans = mid
            if findstart:
                end = mid - 1
            else:
                start = mid + 1
    return ans

def findpos(arr, target):
    ans = [-1, -1]
    startindex = Search(arr, target, True)
    endindex = Search(arr, target, False)

    ans[0] = startindex
    ans[1] = endindex
    return ans

arr = [2, 3, 3, 3, 4 ,6, 7, 8]
target = 3
print(findpos(arr, target))

# Q.5) Find an element in an infinite array. ps you dont know the length in binary seacrh.
# taking chunks of array for the binary search and doubling the size if not found the target.
print("Q.5) --> answer")
def binarysearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        if target == arr[mid]:
            return mid
    return -1

def findele(arr, target):
    start = 0
    end = 2
    flag = 1
    distance = 0
    while flag == 1:
        length = end - start
        ans = binarysearch(arr[start:end], target)
        if ans == -1:
            start = end + 1
            end = end + length*2 + 1
            distance += start
        else:
            flag = 0
            return ans + distance

arr = [1,2,3,4,5,6,7,8,10, 11, 15, 16, 21, 25, 30, 31, 16, 19, 40, 41, 45, 48, 51, 52, 57, 59, 60, 64, 68, 73, 75]
target = 57

print(findele(arr, target))


# Q.6) Find the peak of the mountain array.
# mountain array is arr = [1, 2, 3, 4, 5, 6, 3, 2, 1] peak is 6. 
print("Q.6) --> answer")
def search(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
            start = mid + 1 
        elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
            end = mid - 1
        elif arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
    return -1

arr = [0, 2, 1, 0]
print(search(arr))

# Q.7) Find a target in mountain array.
print("Q.7) --> answer")
def search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
            if target < arr[mid]:
                end = mid - 1
            elif target > arr[mid]:
                start = mid + 1
            else:
                return mid
        elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
            if target < arr[mid]:
                start = mid + 1
            elif target > arr[mid]:
                end = mid - 1
            else:
                return mid
        elif target == arr[mid]:
            return mid
    return -1

arr = [1, 2, 3, 4, 5, 3, 1]
target = 5
print(search(arr, target))

# Q.8) Search in the rotated sorted array.
# Rotated sorted array have pivot points for eg: 
# arr = [3,4,5,6,7,0,1,2]  7 is the pivot point. actuall array befor rotation [0,1,2,3,4,5,6,7]
print("Q.8) --> Answer")

def findpivot(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid
        elif arr[mid] <= arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binaryseacrh(arr, target):
    ind = []
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        if target == arr[mid]:
            return mid
    return -1

def search(arr, target):
    pivot = findpivot(arr)
    left = binaryseacrh(arr[:pivot], target)
    if left == -1:
        return binaryseacrh(arr[pivot:], target)
    else:
        return left
    
arr = [4,5,6,7,0,1,2]
target = 5
print(search(arr, target))

#Q.9) Find the rotation count of an sorted rotated array.
# count will be equal to the pivot + 1
print("Q.9) --> answer")

def rotationcount(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid + 1
        elif arr[mid] <= arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

arr = [15,18,2,3,6,12]
print(rotationcount(arr))