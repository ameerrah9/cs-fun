# Function to find the intersection of two 
# lists using a hash table
def get_intersection(red, blue):
    # set up a hash table to hold the values
    frequency_hash = {}

    # iterate through both lists
    for list in [red, blue]:
        # for each list, iterate through the values
        for item in list:
            # if the value is in the hash table,
            if item in frequency_hash:
                # increment the count
                frequency_hash[item] += 1
            else:
                # otherwise, set the count to 1
                frequency_hash[item] = 1

    # set up a variable to hold the intersections
    intersections = []
    # iterate through the hash table
    for item, quantity in frequency_hash.items():
        # if the quantity is greater than 1,
        if quantity > 1:
            # add the item (key) to the intersections list
            intersections.append(item)

    return intersections

# A function that that takes two strings and returns 
# True if one string is a permutation of the other.
def populate_frequency_map(text):
    frequency_hash = {}
    for char in text:
        if char in frequency_hash:
            frequency_hash[char] += 1
        else:
            frequency_hash[char] = 1
    return frequency_hash


def is_permutation(red, blue):
    red_frequency_hash = populate_frequency_map(red)
    blue_frequency_hash = populate_frequency_map(blue)

    return red_frequency_hash == blue_frequency_hash

# A function that takes a string as an argument and returns 
# True if the letters could be re-arranged into a palindrome.
def is_palindrome_permutation(text):
    frequency_hash = {}
    for char in text:
        if char in frequency_hash:
            frequency_hash[char] += 1
        else:
            frequency_hash[char] = 1

    # count the number of odd matches
    # for each character in the hash table
    odd_matches_count = 0
    # iterate through the values in the hash table
    for frequency in frequency_hash.values():
        # if the frequency is odd,
        if frequency % 2:
            # increment the odd matches count
            odd_matches_count += 1

    return odd_matches_count <= 1