from ..katas.basic_algorithms import *

# Factorial
# Task: Compute the factorial of a number n (e.g., n! = n × (n-1) × … × 1).
# Example: factorial(5) = 120.

def test_factorial():
    expected_1 = factorial(5)
    assert expected_1 == 120

    expected_2 = factorial(0)
    assert expected_2 == 1

    expected_3 = factorial(1)
    assert expected_2 == 1

# Fibonacci
# Task: Compute the nth Fibonacci number.
# Key Points: Demonstrates recursion vs. memoization vs. iterative approaches.

def test_fibonacci():
    expected_1 = fibonacci(5)
    assert expected_1 == 3

    expected_2 = fibonacci(0)
    assert expected_2 == 0

    expected_3 = fibonacci(1)
    assert expected_3 == 1

    expected_4 = fibonacci(9)
    assert expected_4 == 34

    expected_5 = fibonacci(10)
    assert expected_5 == 55

# Permutations / Combinations
# Task: Generate all permutations or combinations of a given list.
# Example: [1, 2, 3] -> permutations: [[1,2,3],[1,3,2],[2,1,3]…].

def test_permutations():
    expected_1 = permutations([1,2,3])
    assert expected_1 == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    expected_2 = permutations([1,2])
    assert expected_2 == [[1,2],[2,1]]

    expected_3 = permutations([1])
    assert expected_3 == [[1]]

# Binary Search
# Task: Given a sorted list, find the index of a target value in O(log n) time. If the target is not in the list, return -1.
# Example: binary_search([1,2,3,4,5], 4) -> 3 (0-based indexing).

def test_binary_search():
    expected_1 = binary_search([1,2,3,4,5], 4)
    assert expected_1 == 3

    expected_2 = binary_search([1,2,3,4,5], 1)
    assert expected_2 == 0

    expected_3 = binary_search([1,2,3,4,5], 5)
    assert expected_3 == 4

    expected_4 = binary_search([1,2,3,4,5], 6)
    assert expected_4 == -1

# Merge Sort (or other sorting)
# Task: Implement merge sort (or quicksort, etc.) for a list of numbers.
# Key Points: Understanding divide-and-conquer and recursion.

def test_merge_sort():
    expected_1 = merge_sort([3,2,1])
    assert expected_1 == [1,2,3]

    expected_2 = merge_sort([3,2,1,4,5])
    assert expected_2 == [1,2,3,4,5]

    expected_3 = merge_sort([1,2,3,4,5])
    assert expected_3 == [1,2,3,4,5]

    expected_4 = merge_sort([5,4,3,2,1])
    assert expected_4 == [1,2,3,4,5]