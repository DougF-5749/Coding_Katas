# 1. Reverse a String
# Description
# Given a string, return the string in reverse order.

# Example:

# Input: "apprentice"
# Output: "ecitnerppa"

# Hints

# You can use Python’s slicing syntax: reversed_str = my_str[::-1].
# Alternatively, you can build the reversed string by iterating backward or using reversed(my_str).













# 2. Check Palindrome
# Description
# Given a string, determine if it is a palindrome (a string that reads the same forward and backward).

# Example:

# Input: "racecar" -> Output: True
# Input: "level" -> Output: True
# Input: "hello" -> Output: False
# Hints

# You can reuse your solution for reversing a string and compare it to the original.
# Convert string to a common case (e.g., all lowercase) if you need a case-insensitive check.












# 3. Count Vowels and Consonants
# Description
# Given a string, count how many vowels (a, e, i, o, u) and how many consonants it contains. (Assume inputs consist of letters only for simplicity, or handle punctuation/spaces by ignoring them.)

# Example:

# Input: "Apprentice" -> Vowels: 4, Consonants: 6
# Hints

# Convert the string to lowercase.
# Use a set of vowels ({'a','e','i','o','u'}) for quick membership checking.
# Increment counters for vowels and consonants accordingly.













# 4. Character Frequency
# Description
# Given a string, return a dictionary (or any data structure you prefer) where each key is a character from the string, and the value is the number of times it appears.

# Example:

# Input: "banana" -> {'b': 1, 'a': 3, 'n': 2}
# Hints

# Python collections.Counter can do this in a single line.
# Or manually loop through each character and update a dictionary.













# 5. Remove Duplicate Characters
# Description
# Write a function that removes any duplicate characters in a given string, keeping only the first occurrence of each character.

# Example:

# Input: "banana" -> "ban"
# Input: "abcaabcd" -> "abcd"
# Hints

# Maintain a set to track seen characters.
# Build a new string by adding characters only if they haven’t been seen before.













# 6. Find the Longest Word in a Sentence
# Description
# Given a sentence, return the longest word (ignoring punctuation). If there are ties, return any one of the longest words.

# Example:

# Input: "This is a test sentence." -> "sentence"
# Hints

# Split the sentence into words (e.g., sentence.split() or using regex).
# Strip punctuation if needed.
# Track the longest word as you iterate.












# 7. Reverse Each Word in a Sentence
# Description
# Given a sentence, reverse each word in place and return the resulting sentence.

# Example:

# Input: "Hello world"
# Output: "olleH dlrow"
# Hints

# Split the sentence, reverse each piece, and then join them back together.
# Watch out for leading/trailing spaces or multiple spaces if that’s in scope.












# 8. String Compression
# Description
# Implement a basic string compression function. For each group of consecutive repeating characters, output <char><number_of_repeats>. If the “compressed” version isn’t shorter, return the original string.

# Example:

# Input: "aaabbc" -> "a3b2c1"
# If the compressed string has the same length or is longer, just return the original.
# Hints

# Iterate through the string, track consecutive characters.
# Build the compressed result as you go.
# Compare lengths at the end.













# 9. First Non-Repeating Character
# Description
# Given a string, find the first character that does not repeat anywhere in the string. If every character repeats, return a special value (e.g., None).

# Example:

# Input: "swiss" -> 'w' (because 's' repeats, 'w' does not repeat)
# Input: "aabb" -> None (no unique character)
# Hints

# Use a dictionary or Counter to count occurrences.
# Then iterate through the string in order and return the first character with a count of 1.












# 10. Generate All Substrings
# Description
# Given a string s, generate all possible substrings of s.

# Example:

# Input: "abc"
# Substrings: "a", "b", "c", "ab", "bc", "abc"
# Hints

# You can use two nested loops:
# Outer loop picks a start index,
# Inner loop picks an end index.
# Mind the indexing carefully (e.g., s[i:j]).










# 11. Validate an Anagram
# Description
# Given two strings, determine if they are anagrams of each other (i.e., if they contain the same letters in the same quantity).

# Example:

# Input: ("listen", "silent") -> True
# Input: ("hello", "olleh") -> True
# Input: ("abc", "abd") -> False
# Hints

# Sort both strings and compare if they’re the same.
# Or count characters in each and compare the dictionaries.













# 12. Convert String to Title Case
# Description
# Given a string, convert it to “title case” format, where the first letter of each word is capitalized, and the rest are lowercase.

# Example:

# Input: "hello WORLD" -> Output: "Hello World"
# Hints

# You can use the built-in .title() method, but be aware that it might not always behave as expected for certain edge cases (apostrophes, etc.).
# Alternatively, split the string into words and capitalize each word manually with .capitalize() or .lower() + .upper() on first letter.











# 13. Remove All Occurrences of a Character
# Description
# Given a string and a character, remove all occurrences of that character from the string.

# Example:

# Input: "banana", "a" -> Output: "bnn"
# Hints

# Use a simple string replace: new_string = original_string.replace(char_to_remove, "").
# Or build a new string in a loop ignoring that character.











# 14. Mask/Obfuscate Part of a String
# Description
# Given a string (e.g., a credit card number or email), replace certain parts of the string with a masking character, for privacy. The rules can vary (for instance, show only the first 2 and last 2 characters, and mask everything in between).

# Example:

# Input: "1234567890" -> Output: "12******90"
# Input: "abcdefg" -> Output: "ab***fg"
# Hints

# Slice the string: keep the unmasked prefix and suffix, and replace the middle with the chosen character repeated enough times.
# Be mindful of edge cases when the string is shorter than the total of prefix + suffix.












# 15. Check if a String Contains All Letters of the Alphabet
# Description
# Determine if the given string is a “pangram”: it contains all 26 letters of the English alphabet at least once.

# Example:

# Input: "The quick brown fox jumps over the lazy dog" -> True
# Input: "Hello world" -> False
# Hints

# Convert the string to lowercase and remove non-letter characters.
# Use a set to collect unique letters. Then check if the set’s size is 26.












# 16. Caesar Cipher Encryption
# Description
# Implement the Caesar cipher, where each letter in the plaintext is shifted by a certain number of positions in the alphabet. Non-alphabetical characters are left as-is.

# Example:

# Input: "abc", shift = 2 -> Output: "cde"
# Input: "xyz", shift = 3 -> Output: "abc"
# Hints

# Use the ASCII code or a string of alphabets.
# Handle wraparound (e.g., after 'z' comes 'a').













# 17. Find the Longest Common Prefix
# Description
# Given a list of strings, find the longest common prefix. If there isn’t one, return an empty string.

# Example:

# Input: ["flower", "flow", "flight"] -> Output: "fl"
# Input: ["dog", "racecar", "car"] -> Output: "" (empty string)
# Hints

# Compare characters of each string position by position.
# Stop at the first mismatch.














# 18. Remove All Non-Alphanumeric Characters
# Description
# Given a string, remove all characters that are not letters or digits (for instance, punctuation, symbols, etc.).

# Example:

# Input: "Hello, World!" -> Output: "HelloWorld"
# Hints

# Use a simple comprehension with char.isalnum()
# Or use regex: re.sub(r'[^a-zA-Z0-9]', '', my_str)













# 19. Find and Replace Pattern in a String
# Description
# Given a string, find a specific pattern (sub-string) and replace it with another string.

# Example:

# Input: string="cats like to chase mice", pattern="cats", replacement="dogs"
# Output: "dogs like to chase mice"
# Hints

# You can use the built-in str.replace(old, new) for a simple find-and-replace.
# For more complex matching (like partial matches or ignoring case), you might use the re module.















# 20. Sort Characters in a String
# Description
# Given a string, return a new string with its characters sorted in ascending alphabetical order.

# Example:

# Input: "cba" -> Output: "abc"
# Input: "banana" -> Output: "aaabnn"
# Hints

# Convert the string to a list of characters, sort, then join back together.
# Or simply do ''.join(sorted(my_str)) in Python.