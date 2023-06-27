# Given 3 strings, return true of false if the third string is a "proper" interleaving of the first two strings.

# Proper means that the characters of the third string preserve the order of the characters from the first two strings.
#
# Example:
# Example Input: "o ev", "TmSro", "Tom Servo"
# Example Output: true


def is_interleaving(str1, str2, str3):
    # compare the first two strings to the third string
    # if the third string is a proper interleaving of the first two strings, return true
    # if the third string is not a proper interleaving of the first two strings, return false

    # validate input
    # check if the length of the first two strings is equal to the length of the third string
    # if not, return false
    if len(str1) + len(str2) != len(str3):
        return False

    # check if the first string is empty
    if len(str1) == 0:
        # if so, check if the second string is equal to the third string
        return str2 == str3

    # check if the second string is empty
    if len(str2) == 0:
        # if so, check if the first string is equal to the third string
        return str1 == str3

    # check if the first character of the first string is equal to the first character of the third string and the first character of the second string is equal to the first character of the third string
    if str1[0] == str3[0] and str2[0] == str3[0]:
        # if so, recursively call is_interleaving on the first string minus the first character, the second string, and the third string minus the first character
        return is_interleaving(str1[1:], str2, str3[1:]) or is_interleaving(
            str1, str2[1:], str3[1:]
        )
    elif str1[0] == str3[0]:
        return is_interleaving(str1[1:], str2, str3[1:])
    elif str2[0] == str3[0]:
        return is_interleaving(str1, str2[1:], str3[1:])
    else:
        return False


print(is_interleaving("haedh", "abras", "haberdash"))
print(is_interleaving("o ev", "TmSro", "Tom Servo"))
