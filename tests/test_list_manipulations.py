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
    assert rotate_list([1, 2, 3, 4, 5], 6) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
    assert rotate_list([1, 2, 3, 4, 5], -6) == [5, 1, 2, 3, 4]

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
    assert partition_list([3, 5, 2, 6, 1], 0) == [3, 5, 2, 6, 1]

# Find All Pairs that Sum to a Target
# Task: Given a list of numbers and a target, find all unique pairs whose sum equals the target.
# Example: [2, 7, 4, 1, 3, 5, 7], target=9 -> Pairs: (2, 7) and (4, 5).

def test_find_all_pairs_that_sum_to_target():
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 9) == [(2, 7), (4, 5)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 10) == [(3, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 11) == [(4, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 12) == [(5, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 13) == []
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 15) == [(7, 7)]
    assert find_all_pairs_that_sum_to_target([2, 7, 4, 1, 3, 5, 7], 16) == []

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