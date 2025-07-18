# Count Word Frequencies
# Task: Given a list of words, build a dictionary mapping each word to its count.
# Example: ["apple", "banana", "apple"] -> {"apple": 2, "banana": 1}.

def count_word_frequencies(lst):
    # APROACH 1
    from collections import Counter
    return Counter(lst)

    # APPROACH 2
    # count = {}

    # for e in lst:
    #     if e not in count:
    #         count[e] = 1
    #     else:
    #         count[e] += 1

    # return count

# Group Anagrams
# Task: Given a list of words, group them together if they are anagrams of each other.
# Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"], ["tan","nat"], ["bat"]].

def most_frequent_word():
    pass

def group_anagrams():
    pass

# Invert a Dictionary
# Task: Swap the keys and values in a dictionary (handle collisions/duplicate values carefully).
# Example: {"a": 1, "b": 2, "c": 3} -> {1: "a", 2: "b", 3: "c"}.

def invert_dictionary(my_dict):
    pass
        

# Find the First Duplicate Character
# Task: Given a string, find the first character that appears more than once using a dictionary to track counts.
# Example: "abca" -> 'a' (first repeated character).

def find_first_duplicate_character():
    pass

# Intersection of Two Dictionaries
# Task: Find keys that appear in both dictionaries and their values (if they match or not).
# Example: {"a":1,"b":2,"c":3} and {"b":2,"c":4,"d":5} -> Intersection is {"b":2} (if we only care about matching key-value pairs).

def intersection_of_two_dictionaries():
    pass