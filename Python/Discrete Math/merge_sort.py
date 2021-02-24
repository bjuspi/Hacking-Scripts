def merge_sort(arr, left, right):
    if left == right:
        return
    else:
        mid = (left + right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, mid+1, right)
    return arr
    
def merge(arr, a_left, a_right, b_left, b_right):
    size = b_right - a_left + 1
    temp = [None]*size
    index = 0
    a_index = a_left
    b_index = b_left

    while (a_index <= a_right) and (b_index <= b_right):
        if arr[a_index] <= arr[b_index]:
            temp[index] = arr[a_index]
            a_index += 1
        else:
            temp[index] = arr[b_index]
            b_index += 1
        index += 1
    while (a_index <= a_right):
        temp[index] = arr[a_index]
        a_index += 1
        index += 1
    while (b_index <= b_right):
        temp[index] = arr[b_index]
        b_index += 1
        index += 1

    for i in range(size):
        arr[a_left + i] = temp[i]