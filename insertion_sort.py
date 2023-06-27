# an implementation of insertion sort
# an algorithm that sorts an array by inserting 
# each item into its correct position in the 
# sorted portion of the array
# array is split into two portions
# the sorted portion and the unsorted portion
# the sorted portion is at the beginning of the array
# the sorted portion is a list into which sorted items are inserted
# the unsorted portion is at the end of the array
# the first item in the array is considered sorted

# in-place sort
# every item after the first item is considered unsorted
# and will be inserted into the sorted portion of the array
# to its proper location in the sorted portion.

# the second item in the array is considered unsorted
# the second item is inserted into the sorted portion of the array
# the third item is considered unsorted
# the third item is inserted into the sorted portion of the array

# a bunch of comparisons are made
# a bunch of swaps are made
# Time complexity: O(n^2)
# Space complexity: O(1)
def insertion_sort(array):
    # Start at the second item in the array
    # the first item is considered sorted
    # i represesnts the first item in the unsorted portion of the array
    i = 1
    # Loop through the unsorted portion of the array
    while i < len(array):
        # Store the first element of the unsorted list in a temporary variable
        # set the insertion index to the current index
        to_insert = array[i]
        # the insertion index will change as the 
        # item is inserted into the sorted portion of the array
        insertion_index = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i] (to_insert in this case is the current item)
        # while the insertion index is greater than 0
        # loop through the sorted list from back to front (backwards)
        # while there are still items in the unsorted portion of the array
        # and while the item to insert is less than the item at the insertion index
        # comparing the item to insert in the sorted portion of the array
        # to the the item in the sorted portion of the array
        # Compare the values between the item at the position we're 
        # inspecting, and the item to insert
        while insertion_index > 0 and array[insertion_index-1] > to_insert:
            # Shift the item at the insertion index to the right
            # swap the new (item to be inserted) item, until we find a value less than the current item.
            array[insertion_index] = array[insertion_index-1]
            # Decrement the insertion index
            # until the item to insert is greater than the item at the insertion index
            insertion_index -= 1
        # Insert the item to insert into the sorted portion of the array
        array[insertion_index] = to_insert
        # Increment the index
        # move to the next item in the unsorted portion of the array
        # Increase the outer index i so that the sorted list grows, 
        # and the unsorted list shrinks
        i += 1

    # Because the original array is modified, no return statement is needed.

## Function to sort an array using
# insertion sort
def insertion_sort2(array):
    i = 0
    key = 0
    j = 0
    # Loop through the array
    # Start at the second item in the array
    for i in range(1,n,1):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1],
        # that are greater than key to
        # one position ahead of their
        # current position
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        
