# an implementation of the bubble sort algorithm
# an algorithm that sorts an array by repeatedly
# swapping the adjacent elements if they are in
# the wrong order
# Time complexity: O(n^2)
# Space complexity: O(1)
def bubble_sort(numbers):
    # store the length of the list in a variable
    length = len(numbers)
    # loop through the list from 0 to the length of the list - 1
    # it is - 1 because the last item in the list does not need to be compared
    # the last item in the list will be the largest number
    for i in range(length - 1):
        # loop through the list from 0 to the length of the list - 1 - i
        # it is - 1 - i because the last i items in the list are already sorted
        # the last i items in the list are the largest numbers
        # so they do not need to be compared
        for j in range(0, length - i - 1):
            # if the number at index j is greater than the number at index j + 1
            # it is greater than the next number in the list
            if numbers[j] > numbers[j + 1]:
                # swap the numbers
                # store the number at index j in a temporary variable
                temp = numbers[j]
                # set the number at index j to the number at index j + 1
                # it is j + 1 because the number at index j is greater than the number at index j + 1
                numbers[j] = numbers[j + 1]
                # set the number at index j + 1 to the number at index j
                numbers[j + 1] = temp

    # return the sorted list
    return numbers