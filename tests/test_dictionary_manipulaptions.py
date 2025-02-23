from katas.dictionary_manipulaptions import *

# Count Word Frequencies
# Task: Given a list of words, build a dictionary mapping each word to its count.
# Example: ["apple", "banana", "apple"] -> {"apple": 2, "banana": 1}.

def test_count_word_frequencies():
    assert count_word_frequencies(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}
    assert count_word_frequencies(["apple", "banana", "apple", "banana", "banana"]) == {"apple": 2, "banana": 3}
    assert count_word_frequencies(["apple"]) == {"apple": 1}
    assert count_word_frequencies([]) == {}
    assert count_word_frequencies(["apple", "banana", "cherry"]) == {"apple": 1, "banana": 1, "cherry": 1}
    assert count_word_frequencies(["apple", "apple", "apple"]) == {"apple": 3}

# Group Anagrams
# Task: Given a list of words, group them together if they are anagrams of each other.
# Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"], ["tan","nat"], ["bat"]].

def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab"]) == [["eat","tea","ate"], ["tan","nat"], ["bat","tab"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba"]) == [["eat","tea","ate"], ["tan","nat"], ["bat","tab","tba"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba","bta"]) == [["eat","tea","ate"], ["tan","nat"], ["bat","tab","tba","bta"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba","bta","atb"]) == [["eat","tea","ate","atb"], ["tan","nat"], ["bat","tab","tba","bta"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba","bta","atb","ant"]) == [["eat","tea","ate","atb"], ["tan","nat","ant"], ["bat","tab","tba","bta"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba","bta","atb","ant","tan"]) == [["eat","tea","ate","atb"], ["tan","nat","ant","tan"], ["bat","tab","tba","bta"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba","bta","atb","ant","tan","ant"]) == [["eat","tea","ate","atb"], ["tan","nat","ant","tan","ant"], ["bat","tab","tba","bta"]]
    assert group_anagrams(["eat","tea","tan","ate","nat","bat","tab","tba","bta","atb","ant","tan","ant","tab"]) == [["eat","tea","ate","atb"], ["tan","nat","ant","tan","ant"], ["bat","tab","tba","bta","tab"]]

# Invert a Dictionary
# Task: Swap the keys and values in a dictionary (handle collisions/duplicate values carefully).
# Example: {"a": 1, "b": 2, "c": 3} -> {1: "a", 2: "b", 3: "c"}.

def test_invert_dictionary():
    assert invert_dictionary({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
    assert invert_dictionary({"a": 1, "b": 2, "c": 3, "d": 1}) == {1: "d", 2: "b", 3: "c"}

# Find the First Duplicate Character
# Task: Given a string, find the first character that appears more than once using a dictionary to track counts.
# Example: "abca" -> 'a' (first repeated character).

def test_find_first_duplicate_character():
    assert find_first_duplicate_character("abca") == 'a'
    assert find_first_duplicate_character("abc") == None
    assert find_first_duplicate_character("abac") == 'a'
    assert find_first_duplicate_character("a") == None
    assert find_first_duplicate_character("aa") == 'a'
    assert find_first_duplicate_character("ab") == None
    assert find_first_duplicate_character("abcabc") == 'a'
    assert find_first_duplicate_character("abcc") == 'c'

# Intersection of Two Dictionaries
# Task: Find keys that appear in both dictionaries and their values (if they match or not).
# Example: {"a":1,"b":2,"c":3} and {"b":2,"c":4,"d":5} -> Intersection is {"b":2} (if we only care about matching key-value pairs).

def test_intersection_of_two_dictionaries():
    assert intersection_of_two_dictionaries({"a":1,"b":2,"c":3}, {"b":2,"c":4,"d":5}) == {"b":2,}
    assert intersection_of_two_dictionaries({"a":1,"b":2,"c":3}, {"b":2,"c":3,"d":5}) == {"b":2, "c":3}
    assert intersection_of_two_dictionaries({"a":1,"b":2,"c":3}, {"b":2,"c":3,"d":5, "a":1}) == {"b":2, "c":3, "a":1}