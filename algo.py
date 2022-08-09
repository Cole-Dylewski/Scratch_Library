
def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = (start + end) // 2
        val = arr[mid]
        print(arr, target, start, mid, end)
        if target == val:
            return mid
        elif target>val:
                start = mid+1
        else:
            end=mid-1

    return -1