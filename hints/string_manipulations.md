# 1. Reverse a String
You can use Python’s slicing syntax: reversed_str = my_str[::-1].
#Alternatively, you can build the reversed string by iterating backward or using reversed(my_str).

# 2. Check Palindrome
You can reuse your solution for reversing a string and compare it to the original.
Convert string to a common case (e.g., all lowercase) if you need a case-insensitive check.

# 3. Count Vowels and Consonants
Convert the string to lowercase.
Use a set of vowels ({'a','e','i','o','u'}) for quick membership checking.
Increment counters for vowels and consonants accordingly.

# 4. Character Frequency
Python collections.Counter can do this in a single line.
Or manually loop through each character and update a dictionary.

# 5. Remove Duplicate Characters
Maintain a set to track seen characters.
Build a new string by adding characters only if they haven’t been seen before.

# 6. Find the Longest Word in a Sentence
Split the sentence into words (e.g., sentence.split() or using regex).
Strip punctuation if needed.
Track the longest word as you iterate.

# 7. Reverse Each Word in a Sentence
Split the sentence, reverse each piece, and then join them back together.
Watch out for leading/trailing spaces or multiple spaces if that’s in scope.

# 8. String Compression
Iterate through the string, track consecutive characters.
Build the compressed result as you go.
Compare lengths at the end.

# 9. First Non-Repeating Character
Use a dictionary or Counter to count occurrences.
Then iterate through the string in order and return the first character with a count of 1.

# 10. Generate All Substrings
You can use two nested loops:
Outer loop picks a start index,
Inner loop picks an end index.
Mind the indexing carefully (e.g., s[i:j]).

# 11. Validate an Anagram
Sort both strings and compare if they’re the same.
Or count characters in each and compare the dictionaries.

# 12. Convert String to Title Case
You can use the built-in .title() method, but be aware that it might not always behave as expected for certain edge cases (apostrophes, etc.).
Alternatively, split the string into words and capitalize each word manually with .capitalize() or .lower() + .upper() on first letter.

# 13. Remove All Occurrences of a Character
Use a simple string replace: new_string = original_string.replace(char_to_remove, "").
Or build a new string in a loop ignoring that character.

# 14. Mask/Obfuscate Part of a String
Slice the string: keep the unmasked prefix and suffix, and replace the middle with the chosen character repeated enough times.
Be mindful of edge cases when the string is shorter than the total of prefix + suffix.

# 15. Check if a String Contains All Letters of the Alphabet
Convert the string to lowercase and remove non-letter characters.
Use a set to collect unique letters. Then check if the set’s size is 26.

# 16. Caesar Cipher Encryption
Use the ASCII code or a string of alphabets.
Handle wraparound (e.g., after 'z' comes 'a').

# 17. Find the Longest Common Prefix
Compare characters of each string position by position.
Stop at the first mismatch.

# 18. Remove All Non-Alphanumeric Characters
Use a simple comprehension with char.isalnum()
Or use regex: re.sub(r'[^a-zA-Z0-9]', '', my_str)

# 19. Find and Replace Pattern in a String
You can use the built-in str.replace(old, new) for a simple find-and-replace.
For more complex matching (like partial matches or ignoring case), you might use the re module.

# 20. Sort Characters in a String
Convert the string to a list of characters, sort, then join back together.
Or simply do ''.join(sorted(my_str)) in Python.