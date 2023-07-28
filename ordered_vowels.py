# Given a word, return whether or not the vowels ("a","e","i","o","u") are in alphabetical order.


def ordered_vowels(word: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_word = []

    for letter in word:
        if letter in vowels:
            vowels_in_word.append(letter)

    return vowels_in_word == sorted(vowels_in_word)


print(ordered_vowels(""))
assert ordered_vowels("continent") == False
