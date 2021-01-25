def subset_sum(arr, k):
    return solve(0, 0, arr, k)

def solve(i, sum, arr, k):
    if i > len(arr)-1:
        if sum == k:
            return True
        else:
            return False
    option1 = solve(i+1, sum+arr[i], arr, k)
    option2 = solve(i+1, sum, arr, k)
    return option1 or option2
