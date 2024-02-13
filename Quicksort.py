# Quick sort using recursion.

def Pass(arr, p):   # THis explains the Pass mechanism for Quick sort.
    s, e = 0, len(arr) - 1
    while (s < e):
        if arr[s] >= p and arr[e] <= p:
            temp = arr[s]
            arr[s] = arr[e]
            arr[e] = temp
            s+=1
            e-=1
    
    return arr

def Quicksort(arr, low, high):
    if low >= high:
        return
    else:
        s = low
        e = high
        p = (e+s)//2
        while (s < e):
            if arr[s] >= arr[p] and arr[e] <= arr[p]:
                temp = arr[s]
                arr[s] = arr[e]
                arr[e] = temp
                s+=1
                e-=1
        
        Quicksort(arr, low, e)
        Quicksort(arr, s+2, high)
        


arr = [5,4,2,3,1]

Quicksort(arr, 0 , len(arr) - 1)

print(arr)
