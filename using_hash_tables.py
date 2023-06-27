# Get Missing Numbers in Range
# Time Complexity: O(n)
def get_missing_numbers_in_range(array, low, high):
    # set up a hash table to hold 
    # the values from the array
    map = {}

    # iterate through the array
    for num in array:
        # add each value to the hash table
        # as a key, with the value set to True
        map[num] = True

    # set up a variable to hold the missing numbers
    missing_nums = []
    # loop through the range of numbers
    # using the low and high values
    for i in range(low, high):
        # if the current number is not in the hash table,
        if i not in map:
            # add it to the missing numbers list
            missing_nums.append(i)

    return missing_nums

# Get Symmetric Pairs
# Time Complexity: O(n)
def get_symmetric_pairs(pairs):
    # set up a hash table to hold the pairs
    pairs_map = {}

    # iterate through the pairs
    for pair in pairs:
        # add each pair to the hash table
        # as a key, with the value set to the other pair
        pairs_map[pair[0]] = pair[1]

    # set up a variable to hold the symmetric pairs
    symmetric_pairs = []

    for pair in pairs:
        # get the key and value from the current pair
        key, val = pair[0], pair[1]
        # if the value is a key in the hash table
        if pairs_map.get(val) == key:
            # add the pair to the symmetric pairs list
            symmetric_pairs.append([key, val])
            # remove the pair from the hash table
            pairs_map.pop(key)

    return symmetric_pairs