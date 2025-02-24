
# 1. Square a Number
- Remember that \(x^2\) in Python is `x * x` or `x ** 2`.


# 2. Check if a Number is Even
- An integer `n` is even if `n % 2 == 0`.

# 3. Return the Last Character of a String
- Use Python’s **negative indexing** or a conditional check if the string is empty.

# 4. Filter Out Vowels from a List of Letters
- Combine a **lambda** with `filter`, or use a list comprehension with a lambda inside if you prefer.
- Remember to handle both uppercase and lowercase if needed.

# 5. Convert a List of Strings to Uppercase
- You can use `map(lambda s: s.upper(), lst)` or a list comprehension.
- The result should be a *list*, so don’t forget to convert from map object to list in Python 3.

# 6. Find the Maximum of a List
- Python’s built-in `max()` can do this directly, but if you want to get fancy, you might use `functools.reduce`.
- Decide how you want to handle an empty list—return `None` or handle errors.

# 7. Remove Duplicates from a List (While Preserving Order)
- You can do this in a single pass using a **seen set**. Consider how to integrate a lambda—maybe within a list comprehension or `filter`.
- Alternatively, think about the **`dict.fromkeys()`** trick for preserving order (in Python 3.7+).

# 8. Check if a String is Palindromic
- A string `s` is a palindrome if `s == s[::-1]`.
- Decide whether you need case-insensitive checks or handling of non-alphanumeric characters.

# 9. Sort a List of Tuples by the Second Item
- Use `sorted(t_list, key=lambda x: x[1])`.
- Consider stable sorting if elements have ties in the second position.

# 10. Compute the Product of All Numbers in a List (Using `reduce`)
- `reduce(lambda x, y: x * y, lst, initial_value)` could be used; if you omit an initial value, be careful with empty lists.
- Alternatively, you can define default behavior (like returning `1` if the list is empty).
