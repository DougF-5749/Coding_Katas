# 🟢 Beginner Katas

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

    assert actual == expected
    assert actual_2 == expected_2

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