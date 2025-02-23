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