# def sort_sentence(s):
#     # Turn string into list
#     s = s.split()

#     # Sort list
#     # Loop through list
#     for i in range(len(s)):
#         # Loop through list again
#         for j in range(len(s)):
#             # Check if i + 1 is in j
#             # Example: "is2" is in "This1"
#             # Where i is the index of the word and j is the index of the word
#             # Check if the number (index plus one) is in the word
#             if str(i + 1) in s[j]:
#                 # Make the word at index i equal to the word at index j
#                 s[i], s[j] = s[j], s[i]

#     s = " ".join(s)

#     for i in s:
#         if i.isdigit():
#             s = s.replace(i, "")

#     return s


def sort_sentence(sentence):
    sentence = sentence.split()
    word_dict = {}
    sorted_sentence = []

    for word in sentence:
        position = word[-1]
        word_dict[position] = word[:-1]

    for position in sorted(word_dict):
        sorted_sentence.append(word_dict[position])

    return " ".join(sorted_sentence)


print(sort_sentence("dear4 excuse2 Sally6 my3 Please1 Aunt5"))

assert sort_sentence("is2 sentence4 This1 a3") == "This is a sentence"
assert sort_sentence("Myself2 Me1 I4 and3") == "Me Myself and I"
print("All tests pass!")
