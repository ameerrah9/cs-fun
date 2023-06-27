# Palindrome
# Write a function that takes a string as an argument and returns True if the string is a palindrome and False otherwise.
"""
    Given a string with capital letters, punctuation and spaces, determine if the sequence is a palindrome. Return true or false.
"""
# Time complexity: O(n)
def is_palindrome(str):
    return str == str[::-1]

# Time complexity: 0(n)
def efficient_palidrome(str):
    # Hold the length of the string in a variable
    length = len(str)
    # Iterate through the string up to the middle
    # // is floor division
    # if the string is odd, the middle character will be ignored
    for i in range(length // 2):
        # if the character at the current index is not equal to the character at the opposite index
        # length - i - 1 is the opposite index
        # where i is the current index
        # e.g. if the string is "bob", i = 0, length = 3, length - i - 1 = 2
        if str[i] != str[length - i - 1]:
            return False
    return True

print(efficient_palidrome("bl o lb"))