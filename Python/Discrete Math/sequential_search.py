# -*- coding: utf-8 -*-

def sequential_search(arr, n):
    result = -1
    for i in range(len(arr)):
        if arr[i] == n:
            result = i
            break
    return result