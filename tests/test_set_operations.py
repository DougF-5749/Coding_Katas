from katas.set_operations import *

# Set Intersection, Union, Difference
# Task: Given two sets, compute their intersection, union, and difference. Return the three sets in a dictionary.
# Example: A = {1,2,3}, B = {2,3,4} -> {Intersection: {2,3}, Union: {1,2,3,4}, Difference: {1}}

def test_intercection_union_difference():
    expected = intercection_union_difference({1,2,3}, {2,3,4})
    assert expected == {'Intersection': {2,3}, 'Union': {1,2,3,4}, 'Difference': {1}}

# Check Disjoint Sets
# Task: Given two sets, determine if they have no elements in common.
# Example: A = {1,3}, B = {2,4} -> Disjoint => True.

def test_disjoint_sets():
    expected = disjoint_sets({1,3}, {2,4})
    assert expected == True

# Find Missing Numbers
# Task: Given a list from which some numbers are missing, find those missing. Using sets can simplify the logic.
# Example: Suppose you expect numbers from 1..10, but only have [1,2,4,7,9]. Missing = {3,5,6,8,10}.

def test_missing_numbers():
    expected = missing_numbers([1,2,4,7,9], 1, 10)
    assert expected == {3,5,6,8,10}

#  Symmetric Difference of Sets
# Task: Given two sets, return the symmetric difference (elements in either set but not in both).  
# Example:  
# A = {1, 2, 3}  
# B = {2, 3, 4}  
# # Symmetric Difference: {1, 4}

def test_symmetric_difference():
    expected_1 = symmetric_difference({1, 2, 3}, {2, 3, 4})
    actual_1 = {1, 4}
    assert expected_1 == actual_1

    expected_2 = symmetric_difference({1, 2, 3, 4}, {2, 3, 4, 5})
    actual_2 = {1, 5}
    assert expected_2 == actual_2

# Subset and Superset Check
# Task: Given two sets, check if one is a subset of the other. Return True if it is, False otherwise.
# Example:  
# A = {1, 2}  
# B = {1, 2, 3, 4}  
# # True

def test_subset():
    expected_1 = subset_superset({1, 2}, {1, 2, 3, 4})
    actual_1 = True

    expected_2 = subset_superset({1, 2, 3, 4}, {1, 2, 3, 4})
    actual_2 = True

    expected_3 = subset_superset({1, 2, 3, 4}, {1, 2, 3})
    actual_3 = False

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3

# Find Common Elements in Multiple Sets
# Task: Given multiple sets, return the common elements among all of them. Rtuen None if there are no common elements. 
# Example:  
# A = {1, 2, 3, 4}  
# B = {2, 3, 4, 5}  
# C = {3, 4, 5, 6}  
# # Common elements: {3, 4}

def test_common_elements():
    expected_1 = common_elements({1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6})
    actual_1 = {3, 4}

    expected_2 = common_elements({1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}, {4, 5, 6, 7})
    actual_2 = {4}

    expected_3 = common_elements({1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}, {5, 6, 7, 8})
    actual_3 = None

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3

# Find Unique Elements Across Multiple Sets
# Task: Given multiple sets, return elements that appear in only one of the sets.  
# Example:  
# A = {1, 2, 3}  
# B = {3, 4, 5}  
# C = {5, 6, 7}  

def test_unique_elements():
    expected_1 = unique_elements({1, 2, 3}, {3, 4, 5}, {5, 6, 7})
    actual_1 = {1, 2, 4, 6, 7}

    expected_2 = unique_elements({1, 2, 3}, {3, 4, 5}, {5, 6, 7}, {1, 2, 3, 4, 5, 6, 7})
    actual_2 = None

    assert expected_1 == actual_1
    assert expected_2 == actual_2

# Count Elements Appearing in At Least Two Sets
# Task: Given multiple sets, count how many of each element appear in at least two of them. reruen the element tyoe and its count in a dictionary. 
# If no elements appear in at least two sets, return an empty -1.
# Example:
# A = {1, 2, 3}
# B = {3, 4, 5}
# C = {5, 6, 7}
# # Elements appearing in at least two sets: {3: 2, 5: 2}

def test_elements_appearing():
    expected_1 = elements_appearing({1, 2, 3}, {3, 4, 5}, {5, 6, 7})
    actual_1 = {3: 2, 5: 2}

    expected_2 = elements_appearing({1, 2, 3}, {3, 4, 5}, {5, 6, 7}, {1, 2, 3, 4, 5, 6, 7})
    actual_2 = {3: 2, 5: 2}

    expected_3 = elements_appearing({1, 2, 3}, {4, 5, 6}, {7, 8, 9})
    actual_3 = -1

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3

# Power Set (All Subsets of a Set)
# Task: Given a set, return all possible subsets (the power set).  
# Example:  
# A = {1, 2}
# # Power set: {(), (1,), (2,), (1,2)}

def test_power_set():
    expected_1 = power_set({1, 2})
    actual_1 = {(), (1,), (2,), (1,2)}

    expected_2 = power_set({1, 2, 3})
    actual_2 = {(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)}

    assert expected_1 == actual_1
    assert expected_2 == actual_2

# Find All Pairs with a Given Sum
# Task: Given a set of numbers and a target sum, return all pairs that sum to that value. Return None if there are no pairs.
# Example:  
# A = {1, 2, 3, 4, 5, 6}  
# target = 7  
# # Pairs: {(1, 6), (2, 5), (3, 4)}

def test_pairs_with_sum():
    expected_1 = pairs_with_sum({1, 2, 3, 4, 5, 6}, 7)
    actual_1 = {(1, 6), (2, 5), (3, 4)}

    expected_2 = pairs_with_sum({1, 2, 3, 4, 5, 6}, 8)
    actual_2 = {(2, 6), (3, 5)}

    expected_3 = pairs_with_sum({1, 2, 3, 4, 5, 6}, 9)
    actual_3 = {(3, 6)}

    expected_4 = pairs_with_sum({1, 2, 3, 4, 5, 6}, 10)
    actual_4 = None

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3
    assert expected_4 == actual_4

# Find the Cartesian Product of Two Sets
# Task: Given two sets, return all possible ordered pairs (Cartesian product).  
# Example:  
# A = {1, 2}  
# B = {3, 4}  
# # Cartesian Product: {(1,3), (1,4), (2,3), (2,4)}

def test_cartesian_product():
    expected_1 = cartesian_product({1, 2}, {3, 4})
    actual_1 = {(1,3), (1,4), (2,3), (2,4)}

    expected_2 = cartesian_product({1, 2, 3}, {4, 5, 6})
    actual_2 = {(1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6)}

    expected_3 = cartesian_product({1, 2, 5}, {0, 1, 4, 5, 6})
    actual_3 = {(1,0), (1,1), (1,4), (1,5), (1,6), (2,0), (2,1), (2,4), (2,5), (2,6), (5,0), (5,1), (5,4), (5,5), (5,6)}

    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3

# Find the Longest Consecutive Sequence in a Set
# Task: Given a set of numbers, find the longest consecutive sequence.  
# Example:  
# A = {100, 4, 200, 1, 3, 2}  
# # Longest sequence: {1, 2, 3, 4}

def test_longest_consecutive_sequence():
    expected_1 = longest_consecutive_sequence({100, 4, 200, 1, 3, 2})
    actual_1 = {1, 2, 3, 4}

    expected_2 = longest_consecutive_sequence({100, 4, 200, 1, 3, 2, 5, 6, 7, 8, 9, 10})
    actual_2 = {5, 6, 7, 8, 9, 10}

    assert expected_1 == actual_1
    assert expected_2 == actual_2
