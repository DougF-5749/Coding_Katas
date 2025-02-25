
# Reverse a List
# Task: Reverse the elements of a list in-place (or return a new reversed list).
# Example: Input [1, 2, 3] -> Output [3, 2, 1].

def reverse_list(list):
    return list[::-1] if len(list) != 0 else None

# Rotate a List
# Task: Shift all elements of a list to the left or right by k positions.
# Example: Rotate [1, 2, 3, 4, 5] right by 2 -> [4, 5, 1, 2, 3].

def rotate_list(list, k):
    k %= len(list)

    if k == 0 or k == len(list):
        return list
    elif k > 0:
        return list[-k:] + list[:-k]
    else:
        return list[k:] + list[:k]

# Remove Duplicates from a non-sorted List
# Task: Given a non-sorted list of intergers, remove duplicates in place and return the a new list.
# Example: [1, 1, 2, 2, 3] -> [1, 2, 3].

def remove_duplicates(list):
    condensed_list = []

    for e in sorted(list):
        if e not in condensed_list:
            condensed_list.append(e)

    return condensed_list

# Merge Two Sorted Lists
# Task: Given two sorted lists, merge them into one sorted list.
# Example: [1, 3, 5] and [2, 4, 6] -> [1, 2, 3, 4, 5, 6].

def merge_sorted_lists(list1, list2):
    return sorted((list1 + list2))

# Move Zeros to the End
# Task: Given a list, move all 0s to the end while maintaining the order of the non-zero elements.
# Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0].

def move_zeros_to_end(lst):
    non_zero_list = [e for e in lst if e != 0]
    zero_lst = [e for e in lst if e == 0] 

    return non_zero_list + zero_lst

# Partition List
# Task: Rearrange elements of a list so that those less than a pivot come before it, and those greater than or equal to the pivot come after it (like the partition step in QuickSort).
# Example: [3, 5, 2, 6, 1] pivot=3 -> [2, 1, 3, 5, 6].

def partition_list():
    pass

# Find All Pairs that Sum to a Target
# Task: Given a list of numbers and a target, find all unique pairs whose sum equals the target.
# Example: [2, 7, 4, 1, 3, 5, 7], target=9 -> Pairs: (2, 7) and (4, 5).

def find_all_pairs_that_sum_to_target():
    pass

# Flatten a Nested List
# Task: Convert a list that may contain nested lists into a single, flat list.
# Example: [1, [2, 3], [4, [5]]] -> [1, 2, 3, 4, 5].

def flatten_nested_list():
    pass

# In-Place Reversal of Sub-List
# Task: Reverse the elements of a sub-list within a larger list, given start and end indices.
# Example: [1, 2, 3, 4, 5], reverse from index 1 to 3 -> [1, 4, 3, 2, 5].

def reverse_sub_list():
    pass