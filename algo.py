
##leetcode 704
##runtime 804ms

def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while start<=end :
        mid = start + ((end -start) // 2)
        val = arr[mid]
        print( target, start, mid, end)
        if target == val:
            return mid
        elif target>val:
                start = mid+1
        else:
            end=mid-1
    return -1


##runtime 494ms
def brute_search_index(arr: list[int],target):
    if target in arr:
        return arr.index(target)
    else:
        return -1