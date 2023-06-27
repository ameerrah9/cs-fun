# Given a sentence, return True if the sentence is a pangram (a sentence that contains all 26 letters). Otherwise, return False. Don't forget your edge cases!

# Example Input: "Fix problem quickly with galvanized jets"
# Example Output: True

# Example Input: "A wizard’s job is to vex chumps quickly in a bog"
# Example Output: False (missing "f")


# Time complexity: O(n)
# Space complexity: O(1)
def is_anagrams(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True


print(is_anagrams(sentence="Fix problem quickly with galvanized jets"))
print(is_anagrams(sentence="A wizard’s job is to vex chumps quickly in a bog"))
# True Pangram
# Given a sentence, return True if the sentence is a true pangram (a sentence that contains all 26 letters once). Otherwise, return False. Don't forget your edge cases!

# Example Input: "Mr. Jock, TV quiz PhD, bags few lynx"
# Example Output: True

# Example Input: "Junk MTV quiz graced by fox whelps"
# Example Output: False (contains duplicate characters)


def is_true_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if sentence.lower().count(char) != 1:
            return False
    return True


print(is_true_pangram(sentence="Mr. Jock, TV quiz PhD, bags few lynx"))
print(is_true_pangram(sentence="Junk MTV quiz graced by fox whelps"))
