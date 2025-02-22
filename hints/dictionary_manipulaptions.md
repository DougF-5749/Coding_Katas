# 1. Count Word Frequencies
- Use a dictionary (in Python, a `dict`) to keep track of how many times each word appears.  
- As you iterate over the list of words, check if the word is already in the dictionary:  
  - If yes, increment its count.  
  - If no, initialize it to 1.  
- Remember to handle edge cases like an empty list (which should result in an empty dictionary).

# 2. Group Anagrams
- Two words are anagrams if their sorted letters are the same. Example: `"tea"` and `"eat"` both become `"aet"` when sorted.  
- Use a dictionary where the key is the “signature” of the word (like the sorted string), and the value is a list of words that match that signature.  
- Iterate over each word:  
  1. Sort the word to get its signature.  
  2. Add the word to the list for that signature in the dictionary.  
- Finally, the values of the dictionary give you the grouped anagrams.

# 3. Invert a Dictionary
- You want to swap keys and values.  
  - For each `(key, value)` in the original dictionary, you will store `(value: key)` in the inverted dictionary.  
- Collision handling: If multiple keys share the same value, you have to decide which key wins in the inverted dictionary or how to handle that. The example shows that the last key that has a repeated value may overwrite previous entries.  
- Make sure you understand the requirements: does your problem explicitly say to overwrite duplicates or keep them somehow?

# 4. Find the First Duplicate Character
- Track characters and their counts (or simply their “seen” status) as you iterate through the string from left to right.  
- As soon as you encounter a character that you have already seen, return it—that’s your first duplicate.  
- If you reach the end of the string without finding a duplicate, return None.  
- Watch out for single-character or empty strings as edge cases.

# 5. Intersection of Two Dictionaries
- You’re looking for keys that appear in both dictionaries *and* potentially have the same value (depending on the requirement).  
- A straightforward approach:  
  1. Loop through one dictionary’s keys.  
  2. Check if each key is in the other dictionary and if the values match (if that’s the criterion).  
  3. If so, add it to the result.  
- Return or print the resulting dictionary containing just the “matching” key-value pairs.  
- Clarify if “intersection” requires matching values or only matching keys.
