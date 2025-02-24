from katas.lambda_functions import *

# 1. Square a Number
# Task: Write a lambda function that takes a single integer `x` and returns its square.
# Example:  
#   ```python
#   square = lambda x: ...
#   print(square(5))  Expected 25
#   ```

def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-5) == 25
    assert square(3) == 9

# 2. Check if a Number is Even
# Task: Write a lambda function that returns `True` if an integer is even, and `False` otherwise.
# Example:
#   ```python
#   is_even = lambda x: ...
#   print(is_even(4))  Expected True
#   print(is_even(5))  Expected False
#   ```

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(0) == True
    assert is_even(-5) == False

# 3. Return the Last Character of a String
# Task: Write a lambda function that takes a string and returns its last character. If the string is empty, return `None` or an empty string.
# Example:
#   ```python
#   last_char = lambda s: ...
#   print(last_char("Hello"))  Expected 'o'
#   print(last_char(""))       Expected None (or '')
#   ```

def test_last_char():
    assert last_char("Hello") == 'o'
    assert last_char("") == None
    assert last_char("a") == 'a'
    assert last_char("abc") == 'c'

# 4. Filter Out Vowels from a List of Letters
# Task: Write a one-line expression that filters out vowels (`a, e, i, o, u`) from a list of letters and returns only the consonants.
# Example:
#   ```python
#   letters = ['a', 'b', 'c', 'e', 'i', 'j']
#   filter_consonants = lambda lst: ...
#   print(filter_consonants(letters))  Expected ['b', 'c', 'j']
#   ```

def test_filter_out_consonants():
    assert filter_out_consonants(['a', 'e', 'i', 'o', 'u']) == []
    assert filter_out_consonants(['A', 'B', 'C', 'E', 'I', 'J']) == ['B', 'C', 'J']
    assert filter_out_consonants(['A', 'E', 'I', 'O', 'U']) == []
    assert filter_out_consonants(['a', 'b', 'c', 'e', 'i', 'j']) == ['b', 'c', 'j']

# 5. Convert a List of Strings to Uppercase
# Task: Given a list of strings, write a lambda (possibly combined with `map`) that returns a new list where each string is uppercase.
# Example:
#   ```python
#   names = ['alice', 'bob', 'charlie']
#   to_upper_list = lambda lst: ...
#   print(to_upper_list(names))  Expected ['ALICE', 'BOB', 'CHARLIE']
#   ```

def test_to_upper_list():
    assert to_upper_list(['alice', 'bob', 'charlie']) == ['ALICE', 'BOB', 'CHARLIE']
    assert to_upper_list(['aLICe', 'BoB', 'CLAIRE']) == ['ALICE', 'BOB', 'CLAIRE']
    assert to_upper_list(['A', 'B', 'C']) == ['A', 'B', 'C']
    assert to_upper_list(['ALICE', 'BOB', 'CHARLIE']) == ['ALICE', 'BOB', 'CHARLIE']

# 6. Find the Maximum of a List
# Task: Write a lambda expression that takes in a list of numbers and returns the maximum value.
# Example:
#   ```python
#   find_max = lambda lst: ...
#   print(find_max([3, 1, 5, 2]))  Expected 5
#   print(find_max([]))           Expected Should handle gracefully (maybe None or a default?)
#   ```

def test_find_max():
    assert find_max([3, 1, 5, 2]) == 5
    assert find_max([1, 2, 3, 4]) == 4
    assert find_max([5]) == 5
    assert find_max([]) == None

# 7. Remove Duplicates from a List (While Preserving Order)
# Task: Given a list, return a new list with **unique** elements, preserving the original order. Use a lambda if possible.
# Example:
#   ```python
#   remove_duplicates = lambda lst: ...
#   print(remove_duplicates([1, 2, 2, 3, 1]))  Expected [1, 2, 3]
#   ```

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert remove_duplicates([4,4,4,10,10,10,31,1,2,3,4,5,6,5,4,5,4,3,2,2,2,2,]) == [4, 10, 31, 1, 2, 3, 5, 6]

# 8. Check if a String is Palindromic
# Task: Write a lambda function that returns `True` if the input string is a palindrome (reads the same forwards and backwards), otherwise `False`.
# Example:
#   ```python
#   is_palindrome = lambda s: ...
#   print(is_palindrome("racecar"))  Expected True
#   print(is_palindrome("hello"))    Expected False
#   ```

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

# 9. Sort a List of Tuples by the Second Item
# Task: Write a lambda to **sort** (or return a sorted copy of) a list of tuples by the **second element** in each tuple.
# Example:
#   ```python
#   tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
#   sort_by_second = lambda t_list: ...
#   print(sort_by_second(tuples))  Expected [(2, 'a'), (1, 'b'), (3, 'c')]
#   ```

def test_sort_by_second():
    assert sort_by_second([(1, 'b'), (2, 'a'), (3, 'c')]) == [(2, 'a'), (1, 'b'), (3, 'c')]
    assert sort_by_second([(1, 'a'), (2, 'b'), (3, 'c')]) == [(1, 'a'), (2, 'b'), (3, 'c')]
    assert sort_by_second([(1, 'c'), (2, 'b'), (3, 'a')]) == [(3, 'a'), (2, 'b'), (1, 'c')]
    assert sort_by_second([(1, 'b'), (2, 'c'), (3, 'a')]) == [(3, 'a'), (1, 'b'), (2, 'c')]

# 10. Compute the Product of All Numbers in a List (Using `reduce`)
# Task: Use a **lambda** with `functools.reduce` to return the product of all elements in a list.

# Example:
#   ```python
#   from functools import reduce
#   product_of_list = lambda lst: ...
#   print(product_of_list([1, 2, 3, 4]))  Expected 24
#   print(product_of_list([5]))          Expected 5
#   print(product_of_list([]))           Expected ?? (decide how to handle)
#   ```

def test_product_of_list():
    assert product_of_list([1, 2, 3, 4]) == 24
    assert product_of_list([5]) == 5
    assert product_of_list([]) == 1
    assert product_of_list([1, 2, 3, 4, 5]) == 120
    assert product_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 362


