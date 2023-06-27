# Function to implement the selection sort
# an algorithm that sorts an array by 
# repeatedly finding the minimum element
# Time complexity: O(n^2)
# Space complexity: O(1)
def selection_sort(lst, n):

    # One by one move boundary of
    # unsorted subarray
    for i in range(n - 1):

        # Find the minimum element
        # in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if (lst[j] < lst[min_idx]):
                min_idx = j

        # Swap the found minimum element
        # with the first element
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
        

