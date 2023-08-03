# Remove the duplicates from an array of unordered integers. Don't return a new array, modify and return the original one.
def remove_duplicates(arr):
    seen = {}
    for num in arr:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1
    i = 0
    while i < len(arr):
        if arr[i] in seen and seen[arr[i]] > 1:
            seen[arr[i]] -= 1
            arr.pop(i)
        else:
            i += 1

    return arr


print(remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7]))
print(remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9]))
