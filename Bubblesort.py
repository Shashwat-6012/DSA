def Bubblesort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i): # i is the pass counter here 
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp

    return arr

def recursivebubble(arr, r, c = 0):
    if r == 0:
        return arr
    if c < r:
            if arr[c] > arr[c+1]:
                temp = arr[c]
                arr[c] = arr[c + 1]
                arr[c+1] = temp
            
            return recursivebubble(arr, r, c+1)
    else:
            return recursivebubble(arr, r-1)


arr = [2, 5, 1, 3, 4]
print(recursivebubble(arr, len(arr)- 1))