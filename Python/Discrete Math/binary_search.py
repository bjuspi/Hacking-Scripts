def binary_search(arr, n):
    result = -1
    left = 0
    right = len(arr)-1

    while((left <= right) and (result == -1)):
        middle = (left + right)//2
        if (n < arr[middle]):
            right = middle - 1
        elif (n > arr[middle]):
            left = middle + 1
        else:
            result = middle
    return result