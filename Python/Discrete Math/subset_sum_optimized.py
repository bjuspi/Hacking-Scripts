def subset_sum_optimized(arr, k):
    return optimized_solve(0, 0, arr, k)

def optimized_solve(i, sum, arr, k):
    if i > len(arr)-1:
        if sum == k:
            return True
        else:
            return False
    if sum > k:
        return False
    option1 = optimized_solve(i+1, sum+arr[i], arr, k)
    option2 = optimized_solve(i+1, sum, arr, k)
    return option1 or option2

    