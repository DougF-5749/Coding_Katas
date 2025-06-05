from katas.recursuion_katas import *

# 🟢 Beginner Katas

# Factorial of a number
#    - Problem: Calculate the factorial of a number using recursion.
#    - Example: factorial(3) -> 6

def test_factorial():
    actual = factorial(3)
    expected = 6

    actual_2 = factorial(5)
    expected_2 = 120

    assert actual == expected
    assert actual_2 == expected_2

# Double values in an array of integers 
#    - Example: double_array([1,2,3,4,5]) -> [2,4,6,8,10]

def test_double_array():
    actual = double_array([1,2,3,4,5])
    expected = [2,4,6,8,10]

    actual_2 = double_array([0,1,2,3,4])
    expected_2 = [0,2,4,6,8]
    
    assert actual == expected
    assert actual_2 == expected_2

# Sum values in an array of integers 
#    - Example: array_sum([1,2,3,4,5]) -> 15

def test_array_sum():
    actual_1 = array_sum([1,2,3,4,5])
    expected_1 = 15

    actual_2 = array_sum([0,1,2,3,4])
    expected_2 = 10

    actual_3 = array_sum([1,2,3,4])
    expected_3 = 10

    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3

# 1️⃣ Sum of Digits (Recursive Digit Sum)
#    - Problem: Given a number, recursively sum its digits until you get a single-digit number.
#    - Example:
#      ```python
#      digital_root(942)  # 9 + 4 + 2 = 15 → 1 + 5 = 6
#      ```

def test_sum_of_digits():
    actual = sum_of_digits(942)
    expected = 6

    actual_2 = sum_of_digits(123)
    expected_2 = 6

    assert actual == expected
    assert actual_2 == expected_2

# 2️⃣ Reverse a String Recursively
#    - Problem: Given a string, return its reverse using recursion.
#    - Example:
#      ```python
#      reverse("hello")  # "olleh"
#      ```

def test_reverse_string():
    actual = reverse_string("hello")
    expected = "olleh"

    actual_2 = reverse_string("goodbye")
    expected_2 = "eybdoog"

    actual_3 = reverse_string("abcde")
    expected_3 = "edcba"

    assert actual == expected
    assert actual_2 == expected_2
    assert actual_3 == expected_3

# Letter count
#   Problem: count the number of a specified letter occurances there are in a given string
#   Example: count_char("axbxcxd") -> 3

def test_count_char():
    actual_1 = count_char("axbxcxd", "x")
    expected_1 = 3

    actual_2 = count_char("axbxcxd", "a")
    expected_2 = 1

    actual_3 = count_char("axbxcxd", "z")
    expected_3 = 0
    
    actual_4 = count_char("", "z")
    expected_4 = 0

    actual_5 = count_char(None, "z")
    expected_5 = 0

    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5

# Total character in array of strings
#   Example: total_chars(["ab", "c", "def", "ghij"]) --> 10

def test_total_chars():
    actual = total_chars(["ab", "c", "def", "ghij"])
    expected = 10

    assert actual == expected

# Return array of even numbers
#   Example: return_evens([1,2,3,4,5]) -> [2,4]

def test_return_evens():
    assert return_evens([1,2,3,4,5]) == [2,4]

# Triangular numbers
#   Example: tri_numbers(7) -> 28
#   Example: tri_numbers(6) -> 21
#   Example: tri_numbers(5) -> 15

def test_tri_numbers():
    assert tri_numbers(7) == 28
    assert tri_numbers(6) == 21
    assert tri_numbers(5) == 15
    assert tri_numbers(4) == 10
    assert tri_numbers(3) == 6
    assert tri_numbers(2) == 3
    assert tri_numbers(1) == 1

# 3️⃣ Power of a Number
#    - Problem: Implement a function to compute \( a^b \) using recursion.
#    - Example:
#      ```python
#      power(2, 3)  # 2^3 = 8
#      ```

def test_power():
    actual = power(2, 3)
    expected = 8

    actual_2 = power(3, 4)
    expected_2 = 81

    assert actual == expected
    assert actual_2 == expected_2

# 🟡 Intermediate Katas

# 4️⃣ Palindrome Check (Recursive)
#    - Problem: Check if a string is a palindrome using recursion.
#    - Example:
#      ```python
#      is_palindrome("racecar")  # True
#      is_palindrome("hello")    # False
#      ```

def test_is_palindrome():
    actual = is_palindrome("racecar")
    expected = True

    actual_2 = is_palindrome("hello")
    expected_2 = False

    assert actual == expected
    assert actual_2 == expected_2

# 5️⃣ Recursive Fibonacci (Optimize with Memoization!)
#    - Problem: Return the nth Fibonacci number using recursion.
#    - Example:
#      ```python
#      fibonacci(6)  # 8
#      ```

def test_fibonacci():
    actual = fibonacci(6)
    expected_1 = 8

    actual_2 = fibonacci(8)
    expected_2 = 21

    assert actual == expected_1
    assert actual_2 == expected_2

# 6️⃣ Flatten a Nested List
#    - Problem: Convert a nested list into a single list.
#    - Example:
#      ```python
#      flatten([1, [2, [3, 4], 5], 6])  # [1, 2, 3, 4, 5, 6]
#      ```

def test_flatten():
    actual = flatten([1, [2, [3, 4], 5], 6])
    expected = [1, 2, 3, 4, 5, 6]

    actual_2 = flatten([1, [2, [3, [4, 5], 6], 7], 8])
    expected_2 = [1, 2, 3, 4, 5, 6, 7, 8]

    assert actual == expected
    assert actual_2 == expected_2

# 🔴 Advanced Katas

# 7️⃣ Tower of Hanoi
#    - Problem: Solve the classic Tower of Hanoi problem with n disks.
#    - Example:
#      ```python
#      tower_of_hanoi(3, 'A', 'C', 'B')  # Moves disks from A to C using B as auxiliary
#      ```

# 8️⃣ Generate All Balanced Parentheses
#    - Problem: Given `n`, generate all combinations of balanced parentheses.
#    - Example:
#      ```python
#      generate_parentheses(3)
#      # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#      ```

# 9️⃣ Permutations of a String
#    - Problem: Generate all possible permutations of a given string.
#    - Example:
#      ```python
#      permutations("abc")
#      # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#      ```

# 🔟 Count Ways to Climb Stairs
#    - Problem: You can take 1 or 2 steps at a time. Given `n` stairs, find the number of ways to reach the top.
#    - Example:
#      ```python
#      count_ways(4)  # Output: 5 (Ways: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2])
#      ```

def test_number_of_paths():
    actual = number_of_paths(4)
    expected = 5

    assert actual == expected