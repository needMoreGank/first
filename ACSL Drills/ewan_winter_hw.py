'''
Name: <yuor name here>
'''

mydict = {"A":1}
print(mydict.items())


'''
1. Word Frequency Counter
Counts the frequency of each word in the provided text.
Input: text (string)
Output: dictionary (key: word, value: frequency)
Example:
word_frequency_counter("Hello World")  # returns {"Hello": 1, "World": 1}
word_frequency_counter("Hello Hello World")  # returns {"Hello": 2, "World": 1}
word_frequency_counter("The quick brown fox jumps over the lazy dog")  # returns {"The": 1, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "the": 1, "lazy": 1, "dog": 1}
'''
def word_frequency_counter(text):
    # Your code here (delete pass)

    "Morgan teaches Python"

    
    """
    To-Do
    1. Make a Dictionary
    2. Convert given string-type text to list.
    3. Actually create algorithm to process list to correct dictionary
    
    """

    word_dict = {}
    text_list = text.split(" ")

    for word in text_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

    

'''
2. Dictionary Combining
Combines two dictionaries into one.
Input: dictionary1, dictionary2
Output: dictionary
Example:
dict1 = {"name": "John", "age": 25}
dict2 = {"height": 180, "weight": 70}
combine_dicts(dict1, dict2)  # returns {"name": "John", "age": 25, "height": 180, "weight": 70}
'''
def combine_dicts(dict1, dict2):
    # Your code here (delete pass)
    pass

'''
3. Dictionary Square Key Values
Write a function named square_key_values that takes in a number and returns a dictionary with the keys as numbers
from 1 to the given number and the values as the square of the keys.
Example:
square_key_values(5)  # returns {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
square_key_values(10)  # returns {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, ... 10: 100}
'''
def square_key_values(number):
    # Your code here (delete pass)
    square_dict = dict()


    for i in range(number):
        i += 1
        square_dict[i] = i**2
        i -= 1
    return square_dict

'''
4. Dictionary List to Dictionary
Write a function named list_to_dict that takes in a list of tuples and returns a dictionary.
Example:
list_to_dict([("name", "John"), ("age", 25)])  # returns {"name": "John", "age": 25}
list_to_dict([("name", "John"), ("age", 25), ("height", 180)])  # returns {"name": "John", "age": 25, "height": 180}
'''
def list_to_dict(lst):
    # Your code here (delete pass)
    pass

'''
5. Set Union
Write a function named set_union that takes in two sets and returns their union.
Example:
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4, 5, 6, 7, 8}
set_union(set_a, set_b)  # returns {1, 2, 3, 4, 5, 6, 7, 8}
'''
def set_union(set_a, set_b):
    # Your code here (delete pass)
    pass

'''
6. Set Intersection
Write a function named set_intersection that takes in two sets and returns their intersection.
Example:
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4, 5, 6, 7, 8}
set_intersection(set_a, set_b)  # returns {2, 3, 4, 5}
'''
def set_intersection(set_a, set_b):
    # Your code here (delete pass)
    # return set_a.intersection(set_b)
    pass


'''
7. Check common elements
Write a Python program to check if two given sets have elements in common.
Example:
set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9, 10}
check_common_elements(set_a, set_b)  # returns False

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
check_common_elements(set_a, set_b)  # returns True
'''
def check_common_elements(set_a, set_b):
    # Your code here (delete pass)
    pass



def test_word_frequency_counter():
    print("Testing word_frequency_counter... ", end="")
    assert word_frequency_counter("Hello World") == {"Hello": 1, "World": 1}
    assert word_frequency_counter("Hello Hello World") == {"Hello": 2, "World": 1}
    assert word_frequency_counter("The quick brown fox jumps over the lazy dog") == {"The": 1, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "the": 1, "lazy": 1, "dog": 1}
    assert word_frequency_counter("The quick brown fox jumps over the lazy dog The dog slept over the verandah") == {"The": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 2, "the": 2, "lazy": 1, "dog": 2, "slept": 1, "verandah": 1}
    print("Passed!")

def test_combine_dicts():
    print("Testing combine_dicts... ", end="")
    dict1 = {"name": "John", "age": 25}
    dict2 = {"height": 180, "weight": 70}
    assert combine_dicts(dict1, dict2) == {"name": "John", "age": 25, "height": 180, "weight": 70}
    dict1 = {"name": "John", "age": 25, "height": 180, "weight": 70}
    dict2 = {"height": 170, "weight": 60}
    assert combine_dicts(dict1, dict2) == {"name": "John", "age": 25, "height": 170, "weight": 60}
    print("Passed!")

def test_square_key_values():
    print("Testing square_key_values... ", end="")
    assert square_key_values(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert square_key_values(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
                                     6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    assert square_key_values(1) == {1: 1}
    print("Passed!")

def test_list_to_dict():
    print("Testing list_to_dict... ", end="")
    assert list_to_dict([("name", "John"), ("age", 25)]) == {"name": "John", "age": 25}
    assert list_to_dict([("name", "John"), ("age", 25), ("height", 180)]) == {"name": "John", "age": 25, "height": 180}
    assert list_to_dict([("name", "John"), ("age", 25), ("height", 180), ("weight", 70)]) == {"name": "John", "age": 25, "height": 180, "weight": 70}
    print("Passed!")

def test_set_union():
    print("Testing set_union... ", end="")
    set_a = {1, 2, 3, 4, 5}
    set_b = {2, 3, 4, 5, 6, 7, 8}
    assert set_union(set_a, set_b) == {1, 2, 3, 4, 5, 6, 7, 8}
    set_a = {1, 2, 3, 4, 5}
    set_b = {6, 7, 8, 9, 10}
    assert set_union(set_a, set_b) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    set_a = {1, 2, 3, 4, 5}
    set_b = {1, 2, 3, 4, 5}
    assert set_union(set_a, set_b) == {1, 2, 3, 4, 5}
    print("Passed!")

def test_set_intersection():
    print("Testing set_intersection... ", end="")
    set_a = {1, 2, 3, 4, 5}
    set_b = {2, 3, 4, 5, 6, 7, 8}
    assert set_intersection(set_a, set_b) == {2, 3, 4, 5}
    set_a = {1, 2, 3, 4, 5}
    set_b = {6, 7, 8, 9, 10}
    assert set_intersection(set_a, set_b) == set()
    print("Passed!")

def test_check_common_elements():
    print("Testing check_common_elements... ", end="")
    set_a = {1, 2, 3, 4, 5}
    set_b = {6, 7, 8, 9, 10}
    assert check_common_elements(set_a, set_b) == False
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    assert check_common_elements(set_a, set_b) == True
    set_a = {1, 2, 3, 4, 5}
    set_b = {1, 2, 3, 4, 5}
    assert check_common_elements(set_a, set_b) == True
    print("Passed!")

def main():
    # Call your functions here to test them
    # Comment out the tests you do not wish to run!
    test_word_frequency_counter()
    test_square_key_values()
    """
    test_combine_dicts()
    
    test_list_to_dict()
    test_set_union()
    test_set_intersection()
    test_check_common_elements()
    """

if __name__ == "__main__":
    main()