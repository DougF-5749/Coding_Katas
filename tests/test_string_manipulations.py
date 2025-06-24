from katas.string_manipulations import *
import time

def test_reverse_string():
    actual = reverse_string("apprentice")
    expected = "ecitnerppa"

    actual_2 = reverse_string("hello")
    expected_2 = "olleh"

    actual_3 = reverse_string("goodbye")
    expected_3 = "eybdoog"

    assert actual == expected
    assert actual_2 == expected_2
    assert actual_3 == expected_3

def test_check_palindrome():
    assert check_palindrome("racecar") == True 
    assert check_palindrome("hello") == False

def test_count_vowels_and_consonants():
    actual_1 = count_vowels_and_consonants("Apprentice")
    expected_1 = "Vowels: 4, Consonants: 6"
    assert actual_1 == expected_1

def test_character_frequency():
    actual = character_frequency("banana")
    expected = {'b': 1, 'a': 3, 'n': 2}

    actual_2 = character_frequency("hello")
    expected_2 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    assert actual == expected
    assert actual_2 == expected_2

def test_remove_duplicate_characters():
    actual = remove_duplicate_characters("banana")
    expected = "ban"

    actual_2 = remove_duplicate_characters("abcaabcd")
    expected_2 = "abcd"

    assert actual == expected
    assert actual_2 == expected_2

def test_find_longest_word_in_sentence():
    actual_1 = find_longest_word_in_sentence("This is a test sentence.")
    expected_1 = "sentence"

    assert actual_1 == expected_1
    
    actual_2 = find_longest_word_in_sentence("This is another test sentence!")
    expected_2 = "sentence"

    assert actual_2 == expected_2
    
    actual_3 = find_longest_word_in_sentence("This sentence contains a hypen-split word")
    expected_3 = "hypen-split"

    assert actual_3 == expected_3
    
    actual_4 = find_longest_word_in_sentence("This, has a comma")
    expected_4 = "comma"

    assert actual_4 == expected_4

def test_reverse_each_word_in_sentence():
    actual = reverse_each_word_in_sentence("Hello world")
    expected = "olleH dlrow"

    assert actual == expected

def test_string_compression():
    actua_1 = string_compression("aaaabbc")
    expected_1 = "a4b2c1"

    actual_2 = string_compression("hello")
    expected_2 = "hello"

    assert actua_1 == expected_1
    assert actual_2 == expected_2

def test_first_non_repeating_character():
    actual_1 = first_non_repeating_character("swiss")
    expected_1 = 'w'

    actual_2 = first_non_repeating_character("aabb")
    expected_2 = None

    actual_3 = first_non_repeating_character("My name is Doug. Most of the time")
    expected_3 = "y"

    actual_4 = first_non_repeating_character("My name is Doug.")
    expected_4 = "M"

    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4

def test_generate_all_substrings():
    actual_1 = generate_all_substrings("abc")
    expected_1 = ["a", "b", "c", "ab", "bc", "abc"]
    
    actual_2 = generate_all_substrings("abcd")
    expected_2 = ["a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", "abcd"]

    assert actual_1 == expected_1
    assert actual_2 == expected_2

def test_validate_anagram():
    assert validate_anagram("listen", "silent") == True
    assert validate_anagram("hello", "olleh") == True
    assert validate_anagram("abc", "abd") == False

def test_convert_string_to_title_case():
    actual = convert_string_to_title_case("hello WORLD")
    expected = "Hello World"

    assert actual == expected

def test_remove_all_occurrences_of_a_character():
    actual = remove_all_occurrences_of_a_character("banana", "a")
    expected = "bnn"

    assert actual == expected

def test_mask_obfuscate_part_of_a_string():
    actual = mask_obfuscate_part_of_a_string("1234567890")
    expected = "12******90"

    actual_2 = mask_obfuscate_part_of_a_string("abcdefg")
    expected_2 = "ab***fg"

#     actual_3 = mask_obfuscate_part_of_a_string("abc")
#     expected_3 = "a*c"

#     actual_4 = mask_obfuscate_part_of_a_string("abcd")
#     expected_4 = "a**d"

#     actual_5 = mask_obfuscate_part_of_a_string("abcde")
#     expected_5 = "a***e"

#     actual_6 = mask_obfuscate_part_of_a_string("a")
#     expected_6 = "*"

    assert actual == expected
    assert actual_2 == expected_2
#     assert actual_3 == expected_3

def test_check_if_string_contains_all_letters_of_the_alphabet():
    assert check_if_string_contains_all_letters_of_the_alphabet("The quick, brown fox jumps over the lazy dog") == True
    assert check_if_string_contains_all_letters_of_the_alphabet("Hello world") == False

def test_caesar_cipher_encryption():
    actual_1 = caesar_cipher_encryption("abc", 2)
    expected_1 = "cde"

    actual_2 = caesar_cipher_encryption("XYZ", 3)
    expected_2 = "ABC"  

    actual_3 = caesar_cipher_encryption("abc", 26)
    expected_3 = "abc"

    actual_4 = caesar_cipher_encryption("a2be", 5)
    expected_4 = "f2gj"

    actual_5 = caesar_cipher_encryption("xyz", 3)
    expected_5 = "abc"  

    actual_6 = caesar_cipher_encryption("abc", 27)
    expected_6 = "bcd"

    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5
    assert actual_6 == expected_6

def test_remove_all_non_alphanumeric_characters():
    actual_1 = remove_all_non_alphanumeric_characters("Hello, World!")
    expected_1 = "HelloWorld"

    actual_2 = remove_all_non_alphanumeric_characters("Hello, World! 123")
    expected_2 = "HelloWorld123"

    assert actual_1 == expected_1
    assert actual_2 == expected_2

def test_find_and_replace_pattern_in_a_string():
    actual = find_and_replace_pattern_in_a_string("cats like to chase mice", "cats", "dogs")
    expected = "dogs like to chase mice"

    assert actual == expected


def test_sort_characters_in_a_string():
    actual = sort_characters_in_a_string("cba")
    expected = "abc"

    actual_2 = sort_characters_in_a_string("banana")
    expected_2 = "aaabnn"

    assert actual == expected
    assert actual_2 == expected_2

def test_sum_numbers_in_string():
    actual_1 = sum_numbers_in_string('')
    expected_1 = None

    actual_2 = sum_numbers_in_string('jdf222sdfk32f3')
    expected_2 = 257

    actual_3 = sum_numbers_in_string('jdf221sdfk32f3k')
    expected_3 = 256
    
    actual_4 = sum_numbers_in_string('d12g3')
    expected_4 = 15
    
    actual_5 = sum_numbers_in_string('123')
    expected_5 = 123
    
    actual_6 = sum_numbers_in_string('abc')
    expected_6 = None
    
    actual_7 = sum_numbers_in_string('a1b-1c')
    expected_7 = 0
    
    actual_8 = sum_numbers_in_string('a1b-1-1c')
    expected_8 = -1
    
    actual_9 = sum_numbers_in_string('a1b-1--1c')
    expected_9 = -1
    
    actual_10 = sum_numbers_in_string('a1b-1--1c--')
    expected_10 = -1

    # actual_11 = sum_numbers_in_string('a1.5--')
    # expected_11 = 1.5

    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5
    assert actual_6 == expected_6
    assert actual_7 == expected_7
    assert actual_8 == expected_8
    assert actual_9 == expected_9
    assert actual_10 == expected_10
    # assert actual_11 == expected_11

def test_sum_numbers_in_string_performance():
    s = '1' + "d" * 10**6 + '2'
    start = time.time()
    result = sum_numbers_in_string(s)
    duration = time.time() - start

    assert result == 3
    assert duration < 0.1 

def test_first_repeating_char():
    assert first_repeating_char("") == None
    assert first_repeating_char("abca") == 3
    assert first_repeating_char("abcdefg") == -1
    assert first_repeating_char("aabbcc") == 1
    assert first_repeating_char("swiss") == 3
    assert first_repeating_char("abdab") == 3

def test_is_valid_parentheses():
    assert is_valid_parentheses("") == True  
    assert is_valid_parentheses("()") == True  
    assert is_valid_parentheses("(") == False  
    assert is_valid_parentheses("()[]{}") ==True  
    assert is_valid_parentheses("(]") == False  
    assert is_valid_parentheses("([)]") == False  
    assert is_valid_parentheses("{[]}") == True  
    assert is_valid_parentheses("]") == False