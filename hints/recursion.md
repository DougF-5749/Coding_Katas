1. **How Recursion Works**
A recursive function has:
- Base Case – The stopping condition to prevent infinite recursion.
- Recursive Case – The function calls itself with a smaller or simpler input.

2. **General Template for Writing Recursive Functions**
```python
def recursive_function(params):
    if base_condition:   # Base case
        return result
    return recursive_function(smaller_params)  # Recursive case
```

3. **Key Points for Recursion**
- Always include a base case to prevent infinite recursion.
- Ensure each recursive call moves towards the base case.
- Be mindful of performance (use memoization if needed).
- Recursion is useful for problems with tree structures, divide-and-conquer, and mathematical problems.

### Below are some hints to help you tackle each recursion kata:

## 🟢 Beginner Katas

### 1️⃣ Sum of Digits (Recursive Digit Sum)
- Hint 1: Start by writing a helper that extracts the last digit using the modulo operator (`n % 10`) and reduces the number with integer division (`n // 10`).
- Hint 2: Define your base case as when the number is less than 10 (i.e., a single digit), then simply return that number.
- Hint 3: Recursively sum the digits and, if the resulting sum is 10 or greater, call the function again with that new sum.

### 2️⃣ Reverse a String Recursively
- Hint 1: Define your base case as when the string is empty or has a length of 1 (in which case it is already reversed).
- Hint 2: For the recursive step, think about breaking the string into the first character and the rest.  
- Hint 3: Return the reverse of the substring (the rest) and then add the first character to the end, i.e., `reverse(s) = reverse(s[1:]) + s[0]`.

### 3️⃣ Power of a Number
- Hint 1: Identify the base case: any number raised to the power of 0 equals 1.
- Hint 2: For the recursive step, multiply the base by the result of a recursive call with the exponent decreased by one, i.e., `power(a, b) = a * power(a, b - 1)`.
- Hint 3: Consider edge cases such as negative exponents or when b is 1.

## 🟡 Intermediate Katas

### 4️⃣ Palindrome Check (Recursive)
- Hint 1: Your base case can be when the string is empty or has only one character (both are inherently palindromes).
- Hint 2: Check if the first and last characters of the string are the same.
- Hint 3: If they match, make a recursive call on the substring obtained by removing these two characters (i.e., `s[1:-1]`).
- Hint 4: If at any step they do not match, return `False`.

### 5️⃣ Recursive Fibonacci (with Memoization)
- Hint 1: Define the base cases: typically, F(0) = 0 and F(1) = 1.
- Hint 2: For n \geq 2, return the sum of the two preceding numbers: `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`.
- Hint 3: Since this approach recomputes values, implement memoization using a dictionary or Python’s `functools.lru_cache` decorator to cache computed Fibonacci numbers.

### 6️⃣ Flatten a Nested List
- Hint 1: Write a recursive function that iterates through each element in the list.
- Hint 2: For each element, check if it’s a list (using `isinstance(item, list)`); if so, recursively flatten it.
- Hint 3: If the element is not a list, add it directly to your result list.
- Hint 4: Combine the results from each recursive call into a single, flat list.

## 🔴 Advanced Katas

### 7️⃣ Tower of Hanoi
- Hint 1: Recognize that the problem is solved by moving the top n-1 disks from the source peg to the auxiliary peg.
- Hint 2: Then move the largest disk (the nth disk) directly to the target peg.
- Hint 3: Finally, move the n-1 disks from the auxiliary peg to the target peg.
- Hint 4: Define the base case for when there is only one disk, which can be moved directly from source to target.
- Hint 5: Think of your recursive function as performing three steps: move, shift, and move again.

### 8️⃣ Generate All Balanced Parentheses
- Hint 1: Use recursion with backtracking: keep track of the count of open and closed parentheses.
- Hint 2: Only add an open parenthesis if you haven’t reached n yet.
- Hint 3: Only add a close parenthesis if it won’t exceed the number of open ones.
- Hint 4: The base case is reached when both counts equal n, at which point the current combination is complete.
- Hint 5: Pass the current state (the string built so far, count of open and closed) in each recursive call.

### 9️⃣ Permutations of a String
- Hint 1: Think of fixing one character and recursively finding all permutations of the remaining substring.
- Hint 2: For each recursive call, insert the fixed character into every possible position in the returned permutations.
- Hint 3: Define your base case when the string length is 1 (or empty), where the permutation is the string itself.
- Hint 4: Alternatively, consider swapping the current index with all other indices recursively.

### 🔟 Count Ways to Climb Stairs
- Hint 1: Recognize that the number of ways to climb n stairs is the sum of the ways to climb n-1 stairs (taking one step) and n-2 stairs (taking two steps).
- Hint 2: Define your base cases carefully: typically, for n = 0 there is 1 way (standing still), and for n = 1 there is 1 way.
- Hint 3: Use recursion to combine these results, and consider memoization if n gets large to avoid redundant calculations.

These hints should give you a good starting point for each problem. Happy coding, and feel free to ask for more guidance or examples as you work through them!