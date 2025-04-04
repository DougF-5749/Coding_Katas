from katas.list_manipulations import *

# Reverse a List
# Task: Reverse the elements of a list in-place (or return a new reversed list).
# Example: Input [1, 2, 3] -> Output [3, 2, 1].

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([1]) == [1]
    assert reverse_list([]) == None

# Rotate a List
# Task: Shift all elements of a list to the left or right by k positions.
# Example: Rotate [1, 2, 3, 4, 5] right by 2 -> [4, 5, 1, 2, 3].

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotate_list([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert rotate_list([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
    assert rotate_list([1, 2, 3, 4, 5], -6) == [2, 3, 4, 5, 1]

# Remove Duplicates from a Sorted List
# Task: Given a non-sorted list of intergers, remove duplicates in place and return the a new list.
# Example: [1, 1, 2, 2, 3] -> [1, 2, 3].

def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 4, 3, 1, 2, 3]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates([]) == []

# Merge Two Sorted Lists
# Task: Given two sorted lists, merge them into one sorted list.
# Example: [1, 3, 5] and [2, 4, 6] -> [1, 2, 3, 4, 5, 6].

def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    assert merge_sorted_lists([1, 3], [2, 4, 6]) == [1, 2, 3, 4, 6]
    assert merge_sorted_lists([1, 3, 5], []) == [1, 3, 5]
    assert merge_sorted_lists([], [2, 4, 6]) == [2, 4, 6]
    assert merge_sorted_lists([], []) == []

# Move Zeros to the End
# Task: Given a list, move all 0s to the end while maintaining the order of the non-zero elements.
# Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0].

def test_move_zeros_to_end():
    assert move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeros_to_end([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert move_zeros_to_end([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert move_zeros_to_end([0, 0, 1, 2, 3]) == [1, 2, 3, 0, 0]
    assert move_zeros_to_end([1, 2, 3, 0, 0]) == [1, 2, 3, 0, 0]
    assert move_zeros_to_end([1, 2, 3, 0, 0, 4, 5]) == [1, 2, 3, 4, 5, 0, 0]

# Partition List
# Task: Rearrange elements of a list so that those less than a pivot come before it, and those greater than or equal to the pivot come after it (like the partition step in QuickSort).
# Example: [3, 5, 2, 6, 1] pivot=3 -> [2, 1, 3, 5, 6].

def test_partition_list():
    assert partition_list([3, 5, 2, 6, 1], 3) == [2, 1, 3, 5, 6]
    assert partition_list([3, 5, 2, 6, 1], 5) == [3, 2, 1, 5, 6]
    assert partition_list([3, 5, 2, 6, 1], 1) == [1, 3, 5, 2, 6]
    assert partition_list([3, 5, 2, 6, 1], 6) == [3, 5, 2, 1, 6]
    assert partition_list([3, 5, 2, 6, -1], 0) == [3, 5, 2, 6, -1]
    assert partition_list([3, 5, 2, 6, 1], 0) == [3, 5, 2, 6, 1]

# Find All Pairs that Sum to a Target
# Task: Given a list of numbers and a target, find all unique pairs whose sum equals the target.
# Example: [2, 7, 4, 1, 3, 5, 7], target=9 -> Pairs: (2, 7) and (4, 5).

def test_find_all_pairs_that_sum_to_target():
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 9) == [(2, 7), (4, 5)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 10) == [(3, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 11) == [(4, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 12) == [(5, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 13) == None
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 16) == None

# Average Even
# Task: Calculate the mean average of all even numbers in a list of numbers
# Example: [1, 2, 3, 4, 5, 6] -> 4

def test_average_even():
    expected_1 = 4
    actual_1 = average_even([1,2,3,4,5,6])

    expected_2 = 3
    actual_2 = average_even([1,2,3,4,5])

    expected_3 = 2
    actual_3 = average_even([1,2,3])

    expected_4 = "No even numbers"
    actual_4 = average_even([1,3,5])

    expected_5 = "No list given"
    actual_5 = average_even([])

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3
    assert expected_4 == actual_4
    assert expected_5 == actual_5

# Word Builder
# Task: Collect every combination of two character strings from a list/array of single characters
# Example: ['a', 'b', 'c', 'd'] -> ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']

def test_word_builder():
    expected_1 = ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
    actual_1 = word_builder(['a', 'b', 'c', 'd'])

    expected_2 = "No list given"
    actual_2 = word_builder([])

    assert expected_1 == actual_1
    assert expected_2 == actual_2

# Get All Two Number Products
# Task: Return an array conataining the priduct of every combination of two numbers from an array of numbers
# Example: [1,2,3,4,5] -> [2,3,4,5,6,8,10,12,15,20]

def test_two_number_products():
    expected_1 = [2,3,4,5,6,8,10,12,15,20]
    actual_1 = two_number_products([1,2,3,4,5])

    expected_2 = "No list given"
    actual_2 = two_number_products([])

    assert expected_1 == actual_1
    assert expected_2 == actual_2

# Two Array Products
# Task: return an array containing the products from every number in one array with every number in a second array
# Example: [1, 2, 3] and [10, 100, 1000] -> [10, 100,1000, 20, 200, 2000, 30, 300, 3000]

def test_two_array_products():
    expected_1 = [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]
    actual_1 = two_array_products([1, 2, 3], [10, 100, 1000])

    expected_2 = "Missing first array"
    actual_2 = two_array_products([], [10, 100, 1000])

    expected_3 = "Missing second array"
    actual_3 = two_array_products([1, 2, 3], [])

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3

# 100-Sum Array
# Task: return True if an array is a 100-Sum array
# [1, 2, 7, 99] -> True
# [2, 2, 98, 99] -> True
# [2, 2, 7, 99] -> False

def test_one_hundred_sum_array():
    expected_1 = True
    actual_1 = one_hundred_sum_array([1, 2, 7, 99])
    
    expected_2 = True
    actual_2 = one_hundred_sum_array([2, 2, 98, 99])

    expected_3 = False
    actual_3 = one_hundred_sum_array([2, 2, 7, 99])

# Merge Sort
# Task: Merge two sorted arrays together to create a new sorted array
# Example: [1, 3, 5] and [2, 4, 6] -> [1, 2, 3, 4, 5, 6]

def test_merge_sort(array_1, array_2):
    expected_1 = [1, 2, 3, 4, 5, 6]
    actual_1 = merge_sort([1, 3, 5], [2, 4, 6])
    
    expected_2 = [1, 2, 3, 4, 5, 6]
    actual_2 = merge_sort([2, 4, 6], [1, 3, 5])

    assert actual_1 == expected_1
    assert actual_2 == expected_2

# Flatten a Nested List
# Task: Convert a list that may contain nested lists into a single, flat list.
# Example: [1, [2, 3], [4, [5]]] -> [1, 2, 3, 4, 5].

def test_flatten_nested_list():
    assert flatten_nested_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten_nested_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_nested_list([1, [2, 3], [4, [5, 6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten_nested_list([1, [2, 3], [4, [5, 6, 7, 8]]]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert flatten_nested_list([1, [2, 3], [4, [5, 6, 7, 8, 9]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten_nested_list([1, [2, 3], [4, [5, 6, 7, 8, 9, 10]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In-Place Reversal of Sub-List
# Task: Reverse the elements of a sub-list within a larger list, given start and end indices.
# Example: [1, 2, 3, 4, 5], reverse from index 1 to 3 -> [1, 4, 3, 2, 5].

def test_reverse_sub_list():
    assert reverse_sub_list([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
    assert reverse_sub_list([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1]
    assert reverse_sub_list([1, 2, 3, 4, 5], 0, 0) == [1, 2, 3, 4, 5]
    assert reverse_sub_list([1, 2, 3, 4, 5], 4, 4) == [1, 2, 3, 4, 5]
    assert reverse_sub_list([1, 2, 3, 4, 5], 2, 3) == [1, 2, 4, 3, 5]