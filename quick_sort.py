# Time complexity: O(n log n)
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array)

    # if the array has 0 or 1 elements, it's already sorted
    if high - low <= 1:
        return

    # partition the current list to find where one element goes
    partition_pos = partition(array, low, high)

    # sort the left and right sides
    quicksort(array, low, partition_pos)
    quicksort(array, partition_pos + 1, high)


def partition(array, low, high):
    # take the last item as the pivot
    last = high - 1
    pivot = array[last]

    # assume pivot will end up at the start
    # conceptually, this position marks the end of the smaller list
    p_index = low

    # iterate over the values not including the pivot
    i = low
    while i < last:
        # if the current value should be to the left of the pivot, swap
        # this value to the potential pivot location and advance that
        # location. conceptually this adds the value to the end of the
        # smaller list and tracks the new end of this list
        if array[i] < pivot:
            temp = array[i]
            array[i] = array[p_index]
            array[p_index] = temp
            p_index += 1
        i += 1

    # swap the pivot value to the end of the smaller list. after this
    # swap, we know that all values to the left of the pivot are smaller,
    # and all values to the right of the pivot are greater or equal
    temp = array[i]
    array[i] = array[p_index]
    array[p_index] = temp

    return p_index
