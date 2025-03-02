# 1. Square a Number
# Task: Write a lambda function that takes a single integer `x` and returns its square.
# Example:  
#   ```python
#   square = lambda x: ...
#   print(square(5))  Expected 25
#   ```

square = lambda x: x*x

# 2. Check if a Number is Even
# Task: Write a lambda function that returns `True` if an integer is even, and `False` otherwise.
# Example:
#   ```python
#   is_even = lambda x: ...
#   print(is_even(4))  Expected True
#   print(is_even(5))  Expected False
#   ```

is_even = lambda num: num % 2 == 0

# 3. Return the Last Character of a String
# Task: Write a lambda function that takes a string and returns its last character. If the string is empty, return `None` or an empty string.
# Example:
#   ```python
#   last_char = lambda s: ...
#   print(last_char("Hello"))  Expected 'o'
#   print(last_char(""))       Expected None (or '')
#   ```

last_char = lambda str: str[-1] if str else None

# 4. Filter Out Vowels from a List of Letters
# Task: Write a one-line expression that filters out vowels (`a, e, i, o, u`) from a list of letters and returns only the consonants.
# Example:
#   ```python
#   letters = ['a', 'b', 'c', 'e', 'i', 'j']
#   filter_consonants = lambda lst: ...
#   print(filter_consonants(letters))  Expected ['b', 'c', 'j']
#   ```

def filter_out_consonants(letters):
    vowels = "aeiouAEIOU"
    return list(filter(lambda e: e not in vowels, letters))

# 5. Convert a List of Strings to Uppercase
# Task: Given a list of strings, write a lambda (possibly combined with `map`) that returns a new list where each string is uppercase.
# Example:
#   ```python
#   names = ['alice', 'bob', 'charlie']
#   to_upper_list = lambda lst: ...
#   print(to_upper_list(names))  Expected ['ALICE', 'BOB', 'CHARLIE']
#   ```

def to_upper_list(string_list):
    return list(map(lambda x: x.upper(), string_list))

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

# MORE - need formatting:
# Below are **10 Lambda Function Kata Challenges** that combine lambda expressions with higher‑order functions like **map** and **filter**. They range from moderate to advanced and encourage chaining transformations for more complex data manipulation.

# ---

# ### 1. Filter Out Even Numbers and Square the Odds

# **Task**:  
# Given a list of integers, use `filter` with a lambda to keep only the odd numbers, then use `map` with a lambda to square each odd number.

# **Example**:  
# Input: `[1, 2, 3, 4, 5]` → Output: `[1, 9, 25]`

# **Hint**:  
# - Use `filter(lambda x: x % 2 != 0, lst)` to select odd numbers.  
# - Then chain with `map(lambda x: x ** 2, ...)` to square them.

# ---

# ### 2. Convert Strings Longer Than 3 Characters to Uppercase

# **Task**:  
# Given a list of strings, use `filter` to keep only strings with length > 3, and then use `map` to convert them to uppercase.

# **Example**:  
# Input: `["hi", "hello", "hey", "welcome"]` → Output: `["HELLO", "WELCOME"]`

# **Hint**:  
# - Filter with: `filter(lambda s: len(s) > 3, lst)`.  
# - Map with: `map(lambda s: s.upper(), ...)`.

# ---

# ### 3. Clean and Lowercase Email Addresses

# **Task**:  
# Given a list of email addresses, use `filter` to remove invalid emails (those not containing `'@'`), then use `map` to convert the valid emails to lowercase.

# **Example**:  
# Input: `["User@Example.com", "bademail.com", "Test@Domain.org"]`  
# → Output: `["user@example.com", "test@domain.org"]`

# **Hint**:  
# - Check validity with: `lambda email: "@" in email`.  
# - Convert to lowercase with: `lambda email: email.lower()`.

# ---

# ### 4. Extract Names with High Scores

# **Task**:  
# Given a list of dictionaries where each dictionary contains keys `"name"` and `"score"`, use `filter` to select only those with a score above a threshold (e.g., 70), then use `map` to extract their names.

# **Example**:  
# Input: `[{"name": "Alice", "score": 85}, {"name": "Bob", "score": 65}]`  
# → Output: `["Alice"]`

# **Hint**:  
# - Use: `filter(lambda d: d["score"] > 70, lst)`.  
# - Then: `map(lambda d: d["name"], ...)`.

# ---

# ### 5. Process Tuples with Multiple Conditions

# **Task**:  
# Given a list of tuples in the form `(number, letter)`, filter those where the number is greater than 10 and the letter is a vowel. Then, use `map` to double the number in each tuple.

# **Example**:  
# Input: `[(12, 'a'), (8, 'e'), (15, 'b'), (20, 'i')]`  
# → Output: `[(24, 'a'), (40, 'i')]`

# **Hint**:  
# - Define a vowel set: `vowels = {'a','e','i','o','u'}`.  
# - Filter with: `lambda t: t[0] > 10 and t[1] in vowels`.  
# - Map with: `lambda t: (t[0] * 2, t[1])`.

# ---

# ### 6. Sum of Sublist Sums Above a Threshold

# **Task**:  
# Given a list of lists of integers, use `map` to compute the sum of each sublist, and then use `filter` to keep only those sums that are greater than a given threshold.

# **Example**:  
# Input: `[[1,2,3], [4,5], [0,0,1]]` with threshold 6  
# → Output: `[6]` (since only the first sublist sums to 6 or more)

# **Hint**:  
# - Map each sublist: `map(lambda sub: sum(sub), lst)`.  
# - Filter with: `filter(lambda total: total > threshold, ...)`.

# ---

# ### 7. Identify and Process Mixed-Type List

# **Task**:  
# Given a list that contains both numbers and strings, use `filter` to extract only the numeric values, then use `map` to square those numbers.

# **Example**:  
# Input: `[1, "apple", 3, "banana", 2]`  
# → Output: `[1, 9, 4]`

# **Hint**:  
# - Check type with: `lambda x: isinstance(x, (int, float))`.  
# - Map with: `lambda x: x ** 2`.

# ---

# ### 8. Tag Words with Their Lengths

# **Task**:  
# Given a list of words, use `map` to transform each word into a tuple `(word, length)`, then use `filter` to keep only those tuples where the length is at least 5.

# **Example**:  
# Input: `["apple", "dog", "banana", "cat"]`  
# → Output: `[("apple", 5), ("banana", 6)]`

# **Hint**:  
# - Map: `map(lambda s: (s, len(s)), lst)`.  
# - Filter: `filter(lambda t: t[1] >= 5, ...)`.

# ---

# ### 9. Chain Multiple Transformations on Numbers

# **Task**:  
# Given a list of integers, chain these operations:  
# 1. Use `map` to add 1 to each number.  
# 2. Use `filter` to keep only numbers divisible by 3.  
# 3. Use `map` to cube the remaining numbers.

# **Example**:  
# Input: `[1, 2, 3, 4, 5]`  
# → After adding 1: `[2, 3, 4, 5, 6]`  
# → Filter divisible by 3: `[3, 6]`  
# → Cube them: `[27, 216]`

# **Hint**:  
# - Chain by assigning intermediate variables or using nested calls.  
# - Example:  
#   ```python
#   result = list(map(lambda x: x**3, filter(lambda x: x % 3 == 0, map(lambda x: x + 1, lst))))
#   ```

# ---

# ### 10. Reverse Valid Alphabetic Words

# **Task**:  
# Given a list of words (strings), use `filter` to remove words containing any non-alphabetic characters, then use `map` to return each remaining word reversed.

# **Example**:  
# Input: `["hello", "world123", "Python", "code!"]`  
# → Output: `["olleh", "nohtyP"]`

# **Hint**:  
# - Filter words with: `lambda w: w.isalpha()`.  
# - Reverse each word with: `lambda w: w[::-1]`.

# ---

# ### Practice Tips

# - **Chain Functions**: You can nest `map` and `filter` calls or use intermediate variables for clarity.  
# - **Edge Cases**: Consider empty lists and unexpected data types.  
# - **Readability**: While lambdas keep your code concise, aim for clarity—sometimes breaking into multiple lines helps.

# Enjoy working through these challenges as you deepen your understanding of lambda functions combined with map and filter!