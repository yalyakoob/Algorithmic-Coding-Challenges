# Given an array of positive numbers and a positive number 'k',
# find the maximum sum of any contiguous subarray of size 'k'

# Example: [2,1,5,1,3,2], k= 3, Output = 9

# Solution

def max_sub_array_of_size_k(k, arr):
    windowSum, windowStart = 0, 0
    max_sum = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            max_sum = max(max_sum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return max_sum
