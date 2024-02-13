arr = [1,5,3,2,6,10,7]

for i in range(0, len(arr)-1):
    last = len(arr) - i - 1
    new_arr = arr[:last+1]
    print("Considered array before swap: ")  # Here the max element is selected and the swap is done with it and the last element.
    print(new_arr)
    maxele = max(new_arr)
    ind = new_arr.index(maxele)
    temp = arr[ind]
    arr[ind] = arr[last]
    arr[last] = temp

print()
print("Final sorted array:")
print(arr)

def recursiveselection(arr, c):
    if c == 0:
        return arr
    last = c
    newarr = arr[:last+1]
    maxele = max(newarr)
    ind = newarr.index(maxele)
    temp = arr[ind]
    arr[ind] = arr[last]
    arr[last] = temp
    return recursiveselection(arr, c-1)

print("Recursive sorted array: ")
print(recursiveselection(arr, len(arr)-1))

