# Set Intersection, Union, Difference
# Task: Given two sets, compute their intersection, union, and difference. Return the three sets in a dictionary.
# Example: A = {1,2,3}, B = {2,3,4} -> {Intersection: {2,3}, Union: {1,2,3,4}, Difference: {1}}

def intercection_union_difference(set1, set2):
    return {
        'Intersection' : set1.intersection(set2),
        'Union' : set1.union(set2),
        'Difference' : set1.difference(set2)
    }

# Check Disjoint Sets
# Task: Given two sets, determine if they have no elements in common.
# Example: A = {1,3}, B = {2,4} -> Disjoint => True.

def disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

# Find Missing Numbers
# Task: Given a list from which some numbers are missing, find those missing. Using sets can simplify the logic.
# Example: Suppose you expect numbers from 1..10, but only have [1,2,4,7,9]. Missing = {3,5,6,8,10}.

def missing_numbers(lst, start, end):
    # APPROACH 1
        # missing = set()
        # lst = set(lst)  # a set is quicker to iterate through that a list with duplicates
        # for num in range(start, end + 1):
        #     if num not in lst:
        #         missing.add(num)
        # return missing
    
    # APPROACH 2 - no loops do better time complexity
        # turn the range into a set
    range_set = set(range(start, end +1))
        # turn the list into a set
    list_set = set(lst)
        # return the difference between the two sets
    return range_set - list_set

#  Symmetric Difference of Sets
# Task: Given two sets, return the symmetric difference (elements in either set but not in both).  
# Example:  
# A = {1, 2, 3}  
# B = {2, 3, 4}  
# # Symmetric Difference: {1, 4}

def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Subset and Superset Check
# Task: Given two sets, check if one is a subset of the other. Return True if it is, False otherwise.
# Example:  
# A = {1, 2}  
# B = {1, 2, 3, 4}  
# # True

def subset():
    pass

# Find Common Elements in Multiple Sets
# Task: Given multiple sets, return the common elements among all of them. Rtuen None if there are no common elements. 
# Example:  
# A = {1, 2, 3, 4}  
# B = {2, 3, 4, 5}  
# C = {3, 4, 5, 6}  
# # Common elements: {3, 4}

def common_elements():
    pass

# Find Unique Elements Across Multiple Sets
# Task: Given multiple sets, return elements that appear in only one of the sets.  
# Example:  
# A = {1, 2, 3}  
# B = {3, 4, 5}  
# C = {5, 6, 7}  

def unique_elements():
    pass

# Count Elements Appearing in At Least Two Sets
# Task: Given multiple sets, count how many of each element appear in at least two of them. reruen the element tyoe and its count in a dictionary. 
# If no elements appear in at least two sets, return an empty -1.
# Example:
# A = {1, 2, 3}
# B = {3, 4, 5}
# C = {5, 6, 7}
# # Elements appearing in at least two sets: {3: 2, 5: 2}

def elements_appearing():
    pass

# Power Set (All Subsets of a Set)
# Task: Given a set, return all possible subsets (the power set).  
# Example:  
# A = {1, 2}
# # Power set: {(), (1,), (2,), (1,2)}

def power_set():
    pass

# Find All Pairs with a Given Sum
# Task: Given a set of numbers and a target sum, return all pairs that sum to that value. Return None if there are no pairs.
# Example:  
# A = {1, 2, 3, 4, 5, 6}  
# target = 7  
# # Pairs: {(1, 6), (2, 5), (3, 4)}

def pairs_with_sum():
    pass

# Find the Cartesian Product of Two Sets
# Task: Given two sets, return all possible ordered pairs (Cartesian product).  
# Example:  
# A = {1, 2}  
# B = {3, 4}  
# # Cartesian Product: {(1,3), (1,4), (2,3), (2,4)}

def cartesian_product():
    pass

# Find the Longest Consecutive Sequence in a Set
# Task: Given a set of numbers, find the longest consecutive sequence.  
# Example:  
# A = {100, 4, 200, 1, 3, 2}  
# # Longest sequence: {1, 2, 3, 4}

def longest_consecutive_sequence():
    pass


