# 🟢 Beginner Katas

# Factorial of a number
#    - Problem: Calculate the factorial of a number using recursion.
#    - Example: factorial(3) -> 6

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Double values in an array of integers 
#    - Example: double_array([1,2,3,4,5]) -> [2,4,6,8,10]

def double_array(array, index=0):
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)
    return array

# Sum values in an array of integers 
#    - Example: array_sum([1,2,3,4,5]) -> 15

def array_sum(array):
    if len(array) == 1:
        return array[0] 
    
    return array[0] + array_sum(array[1:])

# Sum of Digits (Recursive Digit Sum)
#    - Problem: Given a number, recursively sum its digits until you get a single-digit number.
#    - Example:
#      ```python
#      digital_root(942)  # 9 + 4 + 2 = 15 → 1 + 5 = 6
#      ```

def sum_of_digits(num):
    if num < 10:
        return num
    
    digital_sum = sum(int(digit) for digit in str(num))
    return sum_of_digits(digital_sum)

# Reverse a String Recursively
#    - Problem: Given a string, return its reverse using recursion.
#    - Example:
#      ```python
#      reverse("hello")  # "olleh"
#      ```
def reverse_string(string):
    # basecase
    if len(string) == 1:
        return string[0]
    return reverse_string(string[1:]) + string[0]

# Letter count
#   Problem: count the number of a specified letter occurances there are in a given string
#   Example: count_char("axbxcxd") -> 3

def count_char(string, char):
    if not string:
        return 0

    if len(string) == 0:
        return 0 

    if string[0] == char:
        return 1 + count_char(string[1:], char)
    else:
        return count_char(string[1:], char)
    
# Total character in array of strings
#   Example: total_chars(["ab", "c", "def", ghij]) --> 10

def total_chars(array):
    if len(array) == 0:
        return 0
    
    return len(array[0]) + total_chars(array[1:])

# Return array of even numbers
#   Example: return_evens([1,2,3,4,5]) -> [2,4]

def return_evens(array):
    if len(array) == 0:
        return []
    if array[0] % 2 == 0:
        return [array[0]] + return_evens(array[1:])
    else:
        return return_evens(array[1:])
    
# Triangular numbers
#   Example: tri_numbers(7) -> 28
#   Example: tri_numbers(6) -> 21
#   Example: tri_numbers(5) -> 15

def tri_numbers(n):
    if n == 1:
        return 1
    return n + tri_numbers(n-1)

# Index of chacracter:
#   Example: index_of_char("abcdefghijklmnopqrstuvwxyz", "x") -> 23

def index_of_char(string, char):
    if string[0] == char:
        return 0
    
    return index_of_char(string[1:], char) + 1

# Power of a Number
#    - Problem: Implement a function to compute \( a^b \) using recursion.
#    - Example:
#      ```python
#      power(2, 3)  # 2^3 = 8
#      ```

# 🟡 Intermediate Katas

# Palindrome Check (Recursive)
#    - Problem: Check if a string is a palindrome using recursion.
#    - Example:
#      ```python
#      is_palindrome("racecar")  # True
#      is_palindrome("hello")    # False
#      ```

# Recursive Fibonacci (Optimize with Memoization!)
#    - Problem: Return the nth Fibonacci number using recursion.
#    - Example:
#      ```python
#      fibonacci(6)  # 8
#      ```

# def fibonacci(n, memo={}): #RECURSIVE
#     # base case -> the first 2 numbers in the series
#     if n <= 1:
#         return n
#     # check hash table to see if fibonacci(n) was already computed
#     if not memo.get(n):
#         # if n is not in memo, compute finonacci(n) and stoire it in the table
#         memo[n] = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)

#     # return fibonacci(n)'s result which now must be stored in the hash table
#     return memo[n]

def fibonacci(n):
    if n == 0:
        return 0

    a = 0
    b = 1

    for i in range(1,n):
        temp = a
        a = b
        b = temp + a

    return b

# Flatten a Nested List
#    - Problem: Convert a nested list into a single list.
#    - Example:
#      ```python
#      flatten([1, [2, [3, 4], 5], 6])  # [1, 2, 3, 4, 5, 6]
#      ```

# 🔴 Advanced Katas

# Tower of Hanoi
#    - Problem: Solve the classic Tower of Hanoi problem with n disks.
#    - Example:
#      ```python
#      tower_of_hanoi(3, 'A', 'C', 'B')  # Moves disks from A to C using B as auxiliary
#      ```

# Generate All Balanced Parentheses
#    - Problem: Given `n`, generate all combinations of balanced parentheses.
#    - Example:
#      ```python
#      generate_parentheses(3)
#      # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#      ```

# Permutations of a String
#    - Problem: Generate all possible permutations of a given string.
#    - Example:
#      ```python
#      permutations("abc")
#      # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#      ```

# Count Ways to Climb Stairs
#    - Problem: You can take 1 or 2 steps at a time. Given `n` stairs, find the number of ways to reach the top.
#    - Example:
#      ```python
#      count_ways(4)  # Output: 5 (Ways: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2])
#      ```

def number_of_paths(n):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    return number_of_paths(n-1) + number_of_paths(n-2)