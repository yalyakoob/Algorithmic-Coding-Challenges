"""Given a string and a pattern, find all anagrams of the pattern in the given string.
    Write a function to return a list of starting indices of the anagrams of the pattern
    in the given string."""

"""Example:  String="ppqp", Pattern="pq", Output = [1, 2] """


def find_string_anagrams(str1, pattern):
    result_indexes = []
    window_start, matched = 0, 0
    char_frequency = {}
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        if matched == len(pattern):
            result_indexes.append(window_start)
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return result_indexes
