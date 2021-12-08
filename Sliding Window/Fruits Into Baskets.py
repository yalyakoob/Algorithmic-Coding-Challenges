"""Given an array of characters where each character represents a fruit tree,
 you are given two baskets, and your goal is to put maximum number of fruits
  in each basket. The only restriction is that each basket can have only one
   type of fruit. You can start with any tree, but you can’t skip a tree once
    you have started. You will pick one fruit from each tree until you cannot,
    i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both baskets.
"""

"""Example: Fruit=['A','B','C','A','C']. Output = 3 """


def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}
    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in fruit_frequency:
            fruit_frequency[right_char] = 0
        fruit_frequency[right_char] += 1
        while len(fruit_frequency) > 2:
            left_char = fruits[window_start]
            fruit_frequency[left_char] -= 1
            if fruit_frequency[left_char] == 0:
                del fruit_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
