def reverse(arr):
    # Reverse the array
    # Input: [1, 2, 3, 4, 5]
    # Output: [5, 4, 3, 2, 1]
    for i in range(len(arr)//2):
        # set the first index to the last index
        # set the last index to the first index
        # so the first index becomes the last index
        # and the last index becomes the first index
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    
    return arr

def alternative_reverse(arr):
    i = 0
    # set the last index to the length of the array - 1
    j = len(arr) - 1
    
    # while the first index is less than the last index
    while i < j:
        # set the first index to the last index
        # set the last index to the first index
        arr[i], arr[j] = arr[j], arr[i]
        # increment the first index
        i += 1
        # decrement the last index
        j -= 1
    
    return arr

def rotate(arr, shift_by):
    shift_by = shift_by % len(arr)
    
    if shift_by > 0:
        for i in range(shift_by):
            # set the last index to the length of the array - 1
            temp = arr[len(arr)-1]
            # loop through the array backwards
            for j in range(len(arr)-1, 0, -1):
                # set the current index to the previous index
                arr[j] = arr[j-1]
            # set the first index to the last index
            arr[0] = temp

    return arr

# print(reverse([1, 2, 3, 4, 5]))
# print(alternative_reverse([1, 2, 3, 4, 5]))
print(rotate([1, 2, 3, 4, 5], 1)) # [5, 1, 2, 3, 4]