# Brute Force
# A function that takes two arrays as input, 
# and returns True if every value in the second array 
# is present in the first array. 
# The values can be in any order.
def is_subset(arr1, arr2):
    # set up a variable to hold the larger array
    larger_arr = None
    # set up a variable to hold the smaller array
    smaller_arr = None

    # Determine which array is smaller:
    if(len(arr1) > len(arr2)):
        # If arr1 is larger, 
        # set larger_arr to arr1 
        # and smaller_arr to arr2
        larger_arr = arr1
        smaller_arr = arr2
    else:
        # If arr2 is larger,
        # set larger_arr to arr2
        # and smaller_arr to arr1
        larger_arr = arr2
        smaller_arr = arr1

    # Iterate through smaller array
    for i in range(len(smaller_arr)):
        # Assume temporarily the current value from 
        # smaller array is not found in larger array
        found_match = False

    # For each value in smaller array, 
    # iterate through larger array:
    # If the current value in smaller array is 
    # found in larger array,
    # set found_match to True and break out of the loop:
    for j in range(len(larger_arr)):
        if smaller_arr[i] == larger_arr[j]:
            found_match = True
            break

    # If the current value in smaller array 
    # doesn't exist in larger array, return false:
    if not found_match:
        return False

    # If we get to the end of the loops, 
    # it means that all values from smaller 
    # array are present in larger array:
    return True

print(is_subset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f", "h"]))

# Bruteforce
def uncommon_from_sentences(s1, s2):
    # set up a hash table to hold the counts
    counts = {}
    # count the words in each sentence
    count_words(s1, counts)
    count_words(s2, counts) 
    return find_uncommon(counts)

def count_words(sentence, counts):
    for word in sentence.split():
        count = counts.get(word, 0)
        counts[word] = count + 1
        
def find_uncommon(counts):
    # return the words that only appear once
    return [word for word, count in counts.items() if count == 1]

