# Given a string, find the length of the longest substring
# in it with no more than K distinct characters

#Example
# String = "araaci", K=2, Output = 4

#Solution
def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
    return max_length

