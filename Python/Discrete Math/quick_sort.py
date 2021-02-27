def quick_sort(arr, left, right):
    if left >= right:
        return
    else:
        mid = (left+right)//2
        pivot = arr[mid]
        p_left = left
        p_right = right
        while p_left <= p_right:
            while arr[p_left] <= pivot:
                p_left += 1
            while arr[p_right] > pivot:
                p_right -= 1
            if p_left <= p_right:
                arr[p_left], arr[p_right] = arr[p_right], arr[p_left]
                p_left += 1
                p_right -= 1

        quick_sort(arr, left, p_right)
        quick_sort(arr, p_left, right)
        return arr