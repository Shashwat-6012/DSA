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

def recursive_bs(arr, s, e, target) -> int:    # This is a recursive binary search function.
    mid = (s + e)//2
    if target == arr[mid]:
        return 1
    if s > e:
        return -1
    else:
        if target < arr[mid]:
            return recursive_bs(arr, s, mid-1, target)
        else:
            return recursive_bs(arr, mid+1, e, target)
    

arr = [-18, -11, 2, 4, 4, 10, 11, 12, 17]
target = 4
ans = binaryseacrh(arr, 0, len(arr)-1, target)
# ans = binaryseacrh(arr, target)
print(ans)
