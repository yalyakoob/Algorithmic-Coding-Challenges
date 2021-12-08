# Given an array of positive numbers and a positive 'S',
# Find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'
# Return 0 if no such subarray exists

# Example: [2,1,5,2,3,2], S=7, Output = 2
import math


def smallest_subarray_with_given_sum(s, arr):
    window_sum, window_start = 0, 0
    min_length = math.inf
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length



