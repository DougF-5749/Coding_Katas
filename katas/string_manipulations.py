# 1. Reverse a String
# Description
# Given a string, return the string in reverse order.

# Example:

# Input: "apprentice"
# Output: "ecitnerppa"

def reverse_string(string):
    return string[::-1]
    
# 2. Check Palindrome
# Description
# Given a string, determine if it is a palindrome (a string that reads the same forward and backward).

# Example:

# Input: "racecar" -> Output: True
# Input: "level" -> Output: True
# Input: "hello" -> Output: False

def check_palindrome(string):

    # NON-RECURSIVE
    # return string == string[::-1]

    # RECURSIVE
    # define base case
    if len(string) < 2:     # same as if string == "" or len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    return check_palindrome(string[1:-1])



# 3. Count Vowels and Consonants
# Description
# Given a string, count how many vowels (a, e, i, o, u) and how many consonants it contains. (Assume inputs consist of letters only for simplicity, or handle punctuation/spaces by ignoring them.)

# Example:

# Input: "Apprentice" -> Vowels: 4, Consonants: 6

def count_vowels_and_consonants(string):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    # loop though string and check if element is:
    for e in string.lower():
        # isalpha and is in aeiuo
        if e.isalpha() and e in vowels:
            # print(e)
            # v_count += 1
            v_count += 1
        # isalpha and is not in aeiuo
        if e.isalpha and e not in vowels:
            # c_count += 1
            c_count += 1

    return f"Vowels: {v_count}, Consonants: {c_count}"

# 4. Character Frequency
# Description
# Given a string, return a dictionary (or any data structure you prefer) where each key is a character from the string, and the value is the number of times it appears.

# Example:

# Input: "banana" -> {'b': 1, 'a': 3, 'n': 2}

def character_frequency(string):
    freq_dict = {}

    for e in string:
        if e not in freq_dict:
            freq_dict[e] = 1
        elif e in freq_dict:
            freq_dict[e] += 1

    return freq_dict

# 5. Remove Duplicate Characters
# Description
# Write a function that removes any duplicate characters in a given string, keeping only the first occurrence of each character.

# Example:

# Input: "banana" -> "ban"
# Input: "abcaabcd" -> "abcd"

def remove_duplicate_characters(string):
    parsed_string = []
    for char in string:
        if char not in parsed_string:
            parsed_string.append(char)
            
    return "".join(parsed_string)

# 6. Find the Longest Word in a Sentence
# Description
# Given a sentence, return the longest word (ignoring punctuation). If there are ties, return any one of the longest words.

# Example:

# Input: "This is a test sentence." -> "sentence"

def find_longest_word_in_sentence(sentence):
    longest_word = ""

    word_list = [word for word in sentence.split(" ")]

    for char in word_list:
        if char[len(char)-1].isalpha():
            if len(char) > len(longest_word):
                longest_word = char
        else:
            if len(char[:-1]) > len(longest_word):
                longest_word = char[:-1]

    return longest_word

# 7. Reverse Each Word in a Sentence
# Description
# Given a sentence, reverse each word in place and return the resulting sentence.

# Example:

# Input: "Hello world"
# Output: "olleH dlrow"

def reverse_each_word_in_sentence(string):
    # split string into list using " " delimiter
    word_list = string.split(" ")
    # use list comprehsneion to return list of reversed words
    reversed = [word[::-1] for word in word_list]
    # return joined word in list into string using " " delimiter
    return " ".join(reversed)

# 8. String Compression
# Description
# Implement a basic string compression function. For each group of consecutive repeating characters, output <char><number_of_repeats>. 
# If the “compressed” version isn’t shorter, return the original string.

# Example:

# Input: "aaabbc" -> "a3b2c1"
# If the compressed string has the same length or is longer, just return the original.

# THIS PASSES BUT CAN BE REFECTORED LATER vvv

def string_compression(string):
    compressed = ""

    dict = {}
    for char in string:
        if char not in dict:
            dict[char] = 1
        elif char in dict:
            dict[char] += 1

    for tup in dict.items():
        compressed += str(tup[0]) + str(tup[1])

    if len(compressed) >= len(string):
        return string
    else:
        return compressed

# 9. First Non-Repeating Character
# Description
# Given a string, find the first character that does not repeat anywhere in the string. 
# If every character repeats, return a special value (e.g., None).

# Example:

# Input: "swiss" -> 'w' (because 's' repeats, 'w' does not repeat)
# Input: "aabb" -> None (no unique character)

def first_non_repeating_character(string):
    frequency = {}
    non_repeating = []

    # use a dictionary to track frequency of each character 
    for char in string:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    # loop thorugh each string element and check for frequency == 1
    for char in string:
        if frequency[char] == 1:
            # append to non-repeating list
            non_repeating.append(char)

    # return special character if needed
    if len(non_repeating) == 0:
        return None
    # return first element in list
    else:
        return non_repeating[0]

# 10. Generate All Substrings
# Description
# Given a string s, generate all possible substrings of s.

# Example:

# Input: "abc"
# Substrings: "a", "b", "c", "ab", "bc", "abc"

def generate_all_substrings(string):
    substrings = []
    # e.g. 0-3
    for i in range(len(string)):
        # e.g. 1-4
        for j in range(i + 1, len(string) + 1):
            # e.g. [3-4]
            substrings.append(string[i:j])

    # Sort by length first, then by alphabett
    substrings.sort(key=lambda e: (len(e), e))

    return substrings
    
# 11. Validate an Anagram
# Description
# Given two strings, determine if they are anagrams of each other (i.e., if they contain the same letters in the same quantity).

# Example:

# Input: ("listen", "silent") -> True
# Input: ("hello", "olleh") -> True
# Input: ("abc", "abd") -> False

def validate_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# 12. Convert String to Title Case
# Description
# Given a string, convert it to “title case” format, where the first letter of each word is capitalized, and the rest are lowercase.

# Example:

# Input: "hello WORLD" -> Output: "Hello World"

def convert_string_to_title_case(string):
    return string.title()

# 13. Remove All Occurrences of a Character
# Description
# Given a string and a character, remove all occurrences of that character from the string.

# Example:

# Input: "banana", "a" -> Output: "bnn"

def remove_all_occurrences_of_a_character(string, char):
    return "".join(list(filter(lambda x: x != char, string)))

# 14. Mask/Obfuscate Part of a String
# Description
# Given a string (e.g., a credit card number or email), replace certain parts of the string with a masking character, for privacy. 
# The rules can vary (for instance, show only the first 2 and last 2 characters, and mask everything in between).

# Example:

# Input: "1234567890" -> Output: "12******90"
# Input: "abcdefg" -> Output: "ab***fg"

def mask_obfuscate_part_of_a_string(string):
    # element_list = list(string)

    start = string[:2]
    middle = len(string[2:-2]) * "*"
    end = string[-2:]

    return start + middle + end

# 15. Check if a String Contains All Letters of the Alphabet
# Description
# Determine if the given string is a “pangram”: it contains all 26 letters of the English alphabet at least once.

# Example:

# Input: "The quick brown fox jumps over the lazy dog" -> True
# Input: "Hello world" -> False

def check_if_string_contains_all_letters_of_the_alphabet(string):

    alpha_only = [char for char in string.lower() if char.isalpha()]
    
    return len(set(alpha_only)) == 26

# 16. Caesar Cipher Encryption
# Description
# Implement the Caesar cipher, where each letter in the plaintext is shifted by a certain number of positions in the alphabet. 
# Non-alphabetical characters are left as-is.

# Example:

# Input: "abc", shift = 2 -> Output: "cde"
# Input: "xyz", shift = 3 -> Output: "abc"

def caesar_cipher_encryption(string, shift):
    shift %= 26
    encrypted = ""
    for char in string:
        if not char.isalpha():
            encrypted += char
        else:
            ascii = ord(char)
            new_ascii = ascii + shift
            if ((65 <= ascii <= 90) and new_ascii < 91) or ((97 <= ascii <= 122) and new_ascii < 123):
                encrypted += chr(new_ascii)
            if (65 <= ascii <= 90) and new_ascii > 90:
                new_ascii = new_ascii - 26
                encrypted += chr(new_ascii)
            if ((97 <= ascii <= 122) and new_ascii > 122):
                new_ascii = new_ascii - 26
                encrypted += chr(new_ascii)
    return encrypted

# 18. Remove All Non-Alphanumeric Characters
# Description
# Given a string, remove all characters that are not letters or digits (for instance, punctuation, symbols, etc.).

# Example:

# Input: "Hello, World!" -> Output: "HelloWorld"

def remove_all_non_alphanumeric_characters(string):
    filtered_string = ""
    for char in string:
        if char.isalpha() or char.isdigit():
            filtered_string += char
    return filtered_string

# 19. Find and Replace Pattern in a String
# Description
# Given a string, find a specific pattern (sub-string) and replace it with another string.

# Example:

# Input: string="cats like to chase mice", pattern="cats", replacement="dogs"
# Output: "dogs like to chase mice"

def find_and_replace_pattern_in_a_string(string, pattern, replacement):
    if pattern in string:
        return string.replace(pattern, replacement)
    else:
        return -1

# 20. Sort Characters in a String
# Description
# Given a string, return a new string with its characters sorted in ascending alphabetical order.

# Example:

# Input: "cba" -> Output: "abc"
# Input: "banana" -> Output: "aaabnn"

def sort_characters_in_a_string(string):
    return "".join(sorted(list(string)))

def sum_numbers_in_string(string):
    if not string:
        return None
    
    temp_string = ''
    number_array = []

    for i in range(0,len(string)):
        # if the element is char or '-'
        if (string[i].isdigit() or string[i] == '-' or string[i] == "."):
            # check whether element is char or '-'
            if string[i] == '-':
                # if element is '-'
                # check if '-' is already in temp_string
                if '-' not in temp_string:
                    # if '-' not present then add element (which must be '-') to temp_string
                    temp_string += string[i]
                # if '-' is present
                else:
                    if any(char.isdigit() for char in temp_string):
                    # add what is currently in the temp_string to numbers_array
                        number_array.append(float(temp_string))
                    # reset temp_string
                        temp_string = ''
                    # add current '-' symbol to temp_string -> temp_string should now == '-'
                        temp_string += string[i]
            # if string is a digit add digit to temp_string
            else:
                temp_string += string[i]
        if not (string[i].isdigit() or string[i] == '-'):
            if temp_string:
                number_array.append(float(temp_string))
                temp_string = ''

    if temp_string and temp_string != '-':
            number_array.append(float(temp_string))
    
    if number_array:
        return sum(number_array)
    else:
        return None

def min_window(s: str, t: str) -> str:
    pass
