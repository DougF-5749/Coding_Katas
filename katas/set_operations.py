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