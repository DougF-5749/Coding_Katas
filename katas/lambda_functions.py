from katas.lambda_functions import *

# 1. Square a Number
# Task: Write a lambda function that takes a single integer `x` and returns its square.
# Example:  
#   ```python
#   square = lambda x: ...
#   print(square(5))  Expected 25
#   ```

def square():
    pass

# 2. Check if a Number is Even
# Task: Write a lambda function that returns `True` if an integer is even, and `False` otherwise.
# Example:
#   ```python
#   is_even = lambda x: ...
#   print(is_even(4))  Expected True
#   print(is_even(5))  Expected False
#   ```

def is_even():
    pass

# 3. Return the Last Character of a String
# Task: Write a lambda function that takes a string and returns its last character. If the string is empty, return `None` or an empty string.
# Example:
#   ```python
#   last_char = lambda s: ...
#   print(last_char("Hello"))  Expected 'o'
#   print(last_char(""))       Expected None (or '')
#   ```

def last_char():
    pass

# 4. Filter Out Vowels from a List of Letters
# Task: Write a one-line expression that filters out vowels (`a, e, i, o, u`) from a list of letters and returns only the consonants.
# Example:
#   ```python
#   letters = ['a', 'b', 'c', 'e', 'i', 'j']
#   filter_consonants = lambda lst: ...
#   print(filter_consonants(letters))  Expected ['b', 'c', 'j']
#   ```

def filter_out_consonants():
    pass

# 5. Convert a List of Strings to Uppercase
# Task: Given a list of strings, write a lambda (possibly combined with `map`) that returns a new list where each string is uppercase.
# Example:
#   ```python
#   names = ['alice', 'bob', 'charlie']
#   to_upper_list = lambda lst: ...
#   print(to_upper_list(names))  Expected ['ALICE', 'BOB', 'CHARLIE']
#   ```

def to_upper_list():
    pass

# 6. Find the Maximum of a List
# Task: Write a lambda expression that takes in a list of numbers and returns the maximum value.
# Example:
#   ```python
#   find_max = lambda lst: ...
#   print(find_max([3, 1, 5, 2]))  Expected 5
#   print(find_max([]))           Expected Should handle gracefully (maybe None or a default?)
#   ```

def find_max():
    pass

# 7. Remove Duplicates from a List (While Preserving Order)
# Task: Given a list, return a new list with **unique** elements, preserving the original order. Use a lambda if possible.
# Example:
#   ```python
#   remove_duplicates = lambda lst: ...
#   print(remove_duplicates([1, 2, 2, 3, 1]))  Expected [1, 2, 3]
#   ```

def remove_duplicates():
    pass

# 8. Check if a String is Palindromic
# Task: Write a lambda function that returns `True` if the input string is a palindrome (reads the same forwards and backwards), otherwise `False`.
# Example:
#   ```python
#   is_palindrome = lambda s: ...
#   print(is_palindrome("racecar"))  Expected True
#   print(is_palindrome("hello"))    Expected False
#   ```

def is_palindrome():
    pass

# 9. Sort a List of Tuples by the Second Item
# Task: Write a lambda to **sort** (or return a sorted copy of) a list of tuples by the **second element** in each tuple.
# Example:
#   ```python
#   tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
#   sort_by_second = lambda t_list: ...
#   print(sort_by_second(tuples))  Expected [(2, 'a'), (1, 'b'), (3, 'c')]
#   ```

def sort_by_second():
    pass

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

def product_of_list():
    pass
