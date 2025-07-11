from collections import Counter, defaultdict
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
# Task: Rearrange elements of a list so that those less than a pivot come before it, and those greater than or equal to the pivot come after it
# Example: [3, 5, 2, 6, 1] pivot=3 -> [2, 1, 3, 5, 6].

def partition_list(lst, pivot):
    pre_pivot = [e for e in lst if e < pivot]
    after_pivot = [e for e in lst if e > pivot]

    if pivot not in lst:
        return lst
    else:
        return pre_pivot + [pivot] + after_pivot

# Find All Pairs that Sum to a Target
# Task: Given a list of numbers and a target, find all unique pairs whose sum equals the target.
# Example: [2, 7, 4, 1, 3, 5, 7], target=9 -> Pairs: (2, 7) and (4, 5).

def find_all_pairs_that_sum_to_target(num_list, target):
    # BRUTE FORCE
    # pairs = []
    # for i in range(len(num_list)):
    #     for j in range(i, len(num_list)):
    #         if num_list[i] + num_list[j] == target and tuple(sorted((num_list[i], num_list[j]))) not in pairs and num_list[i] != num_list[j]:
    #             pairs.append(tuple(sorted((num_list[i], num_list[j]))))
    # if len(pairs) == 0:
    #     return None
    # else:
    #     return pairs
    
    # HASH MAP ALGORITHM:
    seen = set()            # Keeps track of numbers we've encountered using set
    pairs = []              # Stores all valid pairs in the order we find them

    for num in num_list:
        complement = target - num
        
        if complement in seen:
            # We have found a valid pair (complement, num).
            # complement was in the list before num.
            pair = tuple(sorted((complement, num)))     # sorted tuple means pairs are always given in ascending order
            
            # checjk if we've already recorded this exact pair.
            if pair not in pairs:
                pairs.append(pair)
                
        # Mark the current number as seen.
        seen.add(num)

    # Convert pairs back to a list (or just return pairs, if you prefer) else None
    return pairs if pairs else None


# Average Even
# Task: Calculate the mean average of all even numbers in a list of numbers
# Example: [1, 2, 3, 4, 5, 6] -> 4


# Big O analysis -> worse case: O(3N + 5) -> O(N)
def average_even(lst):
    if not lst:
        return "No list given"

    sum = 0
    count = 0

    for i in lst:
        if i % 2 == 0:
            sum += i
            count += 1
    
    return sum // count if count > 0 else "No even numbers"

# Word Builder
# Task: Collect every combination of two character strings from a list/array of single characters
# Example: ['a', 'b', 'c', 'd'] -> ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']

# Big O time analysis -> A nested loop both rotating though whole list -> O(N^2)
def word_builder(lst):
    
    if not lst:
        return "No list given"
    
    collection = []

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                collection.append(lst[i] + lst[j])

    return collection

# Get All Two Number Products
# Task: Return an array conataining the priduct of every combination of two numbers from an array of numbers
# Example: [1,2,3,4,5] -> [2,3,4,5,6,8,10,12,15,20]

# Big O time analysis -> (N - 1) + (N - 2) + ... + 1 -> N(N - 1)/2 -> O(N²)
def two_number_products(array):
    
    if not array:
        return "No list given"
    
    products = []

    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            products.append(array[i] * array[j])
    
    return products

# Two Array Products
# Task: return an array containing the products from every number in one array with every number in a second array
# Example: [1, 2, 3] and [10, 100, 1000] -> [10, 100,1000, 20, 200, 2000, 30, 300, 3000]

# Big O time analysis -> 4NM + 4 -> O(M*N) bilinear time
# Two different arrays so cant say N^2 (even though we know they are the same length in the test)
def two_array_products(array_1, array_2):
    if not array_1:
        return "Missing first array"
    if not array_2:
        return "Missing second array"
    
    products = []
    
    for i in range(len(array_1)):
        for j in range(len(array_2)):
            products.append(array_1[i] * array_2[j])
    
    return products

# 100-Sum Array
# Task: return True if an array is a 100-Sum array
# [1, 2, 7, 99] -> True
# [2, 2, 98, 99] -> True
# [2, 2, 7, 99] -> False

def one_hundred_sum_array(array):
# RECURSIVE - O(N^2)
    # if len(array) < 2:
    #     return False
    # if array[0] + array[-1] == 100:
    #     return True
    # return one_hundred_sum_array(array[1:-1])
# NON-RECURSIVE time analysis: N/2 -> O(N)
    left_index = 0
    right_index = len(array) - 1

    while left_index < (len(array) / 2):
        if array[left_index] + array[right_index] != 100:
            return False
        left_index += 1
        right_index -= 1
        
    return True

# INtersection of two arrays
# Task: Write a function that returns the interesction of two arrays. The intersection is  third array that contains all the values contained in the first two arrays
# Example: [1,2,3,4,5] and [0,2,4,6,8] -> [2,4]

def get_intersection(array_1, array_2):
    hash_table = {}
    intersection = []

    for e in array_1:
        hash_table[e] = True

    for e in array_2:
        if hash_table.get(e):   
        # use .get() rather than direct access to aboid KeyError as .get() returns None if key not in dictionary
            intersection.append(e)

    return intersection

# return first duplicate
# Task: Write a function that takes an array of strings and returns the first duplicate value it finds
# Example: ["a", "b", "c", "d", "c", "e", "f"] -> "c"

def return_first_duplicate(array):
    if not array:
        return None
    
    seen_hash = {}

    for e in array:
        if seen_hash.get(e):
            return e
        else:
            seen_hash[e] = True

    return None

# Missing alphabet character
# Task: Write a function that accepts a string that contains all the letters of the...
# alphabet except one and returns the missing letter
# Example: "the quick brown box jumps over the lazy dog" -> "f"

def missing_alpha(string):
    if not string:
        return None
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    hash_map = {}

    for char in string.lower():
        hash_map[char] = True
    
    for char in alpha:
        if not hash_map.get(char):
            return char
    return None

# Non-duplicated haracter in string
# Task: Return the first non-duplicated character in a string.
# Example: "minimum" -> "n"

def first_non_duplicated(string):
    if not string:
        return None

    seen_hash_map = {}

    for e in string:
        if not seen_hash_map.get(e):
            seen_hash_map[e] = 1
        else:
            seen_hash_map[e] += 1
    
    for e in string:
        if seen_hash_map[e] == 1:
            return e

# Problem: Given a list of integers nums, return the element that appears more than ⌊n / 2⌋ times. 
    # You may assume that the majority element always exists in the input.
# Examples: 
    # majority_element([3, 2, 3])            -> 3
    # majority_element([2, 2, 1, 1, 1, 2, 2]) -> 2
    # majority_element([1])                  -> 1

def majority_element(nums):
    nums_count = Counter(nums)
    length = len(nums) / 2
        
    for num, count in nums_count.items():
        if count > length:
            return num
        
# Given a list of strings, group the anagrams together. 
# Return a list of groups, where each group is a list of strings that are anagrams of each other.
# Examples:
    # group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(words: list) -> list[list[str]]:
    groups = []
    hash_map = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        hash_map[sorted_word].append(word)
    #     if not hash_map.get(sotred_string):
    #         hash_map[sotred_string] = [lst[i]]
    #     else:
    #         hash_map[sotred_string].append(lst[i])
    
    for val in hash_map.values():
        groups.append(val)

    return groups







# Merge Sort
# Task: Merge two sorted arrays together to create a new sorted array
# Example: [1, 3, 5] and [2, 4, 6] -> [1, 2, 3, 4, 5, 6]

def merge_sort(array_1, array_2):
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