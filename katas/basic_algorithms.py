# Factorial
# Task: Compute the factorial of a number n (e.g., n! = n × (n-1) × … × 1).
# Example: factorial(5) = 120.

def factorial():
    pass

# Fibonacci
# Task: Compute the nth Fibonacci number.
# Key Points: Demonstrates recursion vs. memoization vs. iterative approaches.

def fibonacci():
    pass

# Permutations / Combinations
# Task: Generate all permutations or combinations of a given list.
# Example: [1, 2, 3] -> permutations: [[1,2,3],[1,3,2],[2,1,3]…].

def permutations():
    pass

# Binary Search
# Task: Given a sorted list, find the index of a target value in O(log n) time. 
# If the target is not in the list, return -1.
# Example: binary_search([1,2,3,4,5], 4) -> 3 (0-based indexing).

def binary_search(lst, search_value):
    # establish lower sand upper bounds of search range (0th and last index of the list)
    lower_bound = 0
    upper_bound = len(lst) - 1

    # loop to instect the middlemost value - "lower_bound <= upper_bound" means loop ends if tghere is no range left to inspect
    while lower_bound <= upper_bound:
        # floor divide (//) to account for odd list length
        midpoint = (lower_bound + upper_bound) // 2
        # inspect the list midpoint and assign it to midpoint variable
        value_at_midpoint = lst[midpoint]

        # if value at midpoint is what we are looking for, return its index.
        if search_value == value_at_midpoint:
            return midpoint
        # search value is less than midpoint (i.e. earlier in the list)
        elif search_value < value_at_midpoint:
            #  change upper bound for nexct loop immediately to left of current midpoint
            upper_bound = midpoint - 1
        # search value is greater than midpoint (i.e. later in the list)
        elif search_value > value_at_midpoint:
            #  change lower bound for next loop immediately to right of current midpoint
            lower_bound = midpoint + 1
    
    # if range is narrowed to 0 elements, search value is not in the list. return -1
    return -1

# Merge Sort (or other sorting)
# Task: Implement merge sort (or quicksort, etc.) for a list of numbers.
# Key Points: Understanding divide-and-conquer and recursion.

def merge_sort(lst):
    # bubble sort (quadratic time)
    unsorted_until_index = len(lst) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False
        unsorted_until_index -= 1
    return lst