# an efficient algorithm for finding an item in a sorted list.
# It works by repeatedly dividing in half the portion of the
# list that could contain the item, until you've narrowed
# down the possible locations to just one

# Time complexity: O(log n)
# Space complexity: O(1)
# the list must be sorted
time = {"count": 0}


def binary_search(array, value):
    # set the low and high indices

    # low is the first index
    low = 0
    # high is the last index
    # len(array) - 1 because the index starts at 0
    # and the length of the array is 1 more than the last index

    # e.g. array = [1, 2, 3, 4, 5]
    # len(array) = 5
    # last index = 4
    # len(array) - 1 = 4
    # high = 4
    # array[4] = 5
    # array[5] = IndexError: list index out of range
    # array[4] is the last item in the array
    high = len(array) - 1  # high is the last index

    # while the low index is less than or equal to the high index
    while low <= high:
        # find the middle index by adding the low and high indices and dividing by 2

        # e.g. 0 + 4 = 4
        # 4 // 2 = 2
        # 2 is the middle index
        # array[2] = 3
        mid = (low + high) // 2
        time += 1
        # once the middle index is found check
        # if the value at the middle index is
        # greater than the value we are searching for
        # e.g. array[mid] = 3
        # value = 4
        # 3 > 4 = False
        if array[mid] > value:
            # if the value at the middle index is greater than the value we are searching for
            # set the high index to the middle index - 1
            # so the next time the loop runs the high index will be 1 less than the previous high index
            high = mid - 1
        # if the value at the middle index is less than the value we are searching for
        elif array[mid] < value:
            # set the low index to the middle index + 1
            # so the next time the loop runs the low index will be 1 more than the previous low index
            low = mid + 1
        # if the value at the middle index is equal to the value we are searching for
        else:
            # return the middle index
            return mid

        # if the value is equal to the value at the low index
        # return the low index
        # so if the value is the first item in the array
        if array[low] == value:
            return low
    # if the value is not in the array
    # return None
    # some people return -1
    print("hello")


binary_search([1, 3, 5, 17, 30], 5)


# Another Example
# Recursive Binary Search
def binary_search(data, query):
    if not data:
        return False

    mid = len(data) // 2

    if query == data[mid]:
        return True
    elif query < data[mid]:
        data = data[:mid]
    elif query > data[mid]:
        data = data[mid + 1 :]

    return binary_search(data, query)
