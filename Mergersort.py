def Merge(left, right):
    ans = []
    i, j, k = 0, 0, 0
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
        
    # appending the remaining elements as it is
    
    while(i < len(left)):
        ans.append(left[i])
        i +=1 
    while(j < len(right)):
        ans.append(right[j])
        j+=1
    
    return ans

def Mergesort(arr):
    mid = (len(arr))//2 
    if len(arr) == 1:
        return arr 
    left = Mergesort(arr[:mid])
    right = Mergesort(arr[mid:])

    return Merge(left, right)

arr1 = [3, 4, 8, 11, 20]
arr2 = [5,6,10]

print(Merge(arr1,arr2))