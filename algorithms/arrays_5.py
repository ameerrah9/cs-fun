def nth_largest_num(lst, n):
    sorted_lst = sorted(lst)
    
    # if the length of the list is less than n
    # return None
    # because there is no nth largest number
    # -n is the index of the nth largest number
    try:
        return sorted_lst[-n]
    except:
        return None
# Time complexity: O(n)
# Space complexity O(n)

def remove_range(lst, start_el, end_el):
    # loop over the list in reverse order
    # start from the end_el and end at the start_el minus 1
    # minus 1 because the range function is exclusive
    # remove the element at the current index
    # -1 is the step size
    # range(start, stop, step)
    # range(5, 0, -1) -> 5, 4, 3, 2, 1
    # Example: remove_range([20, 30, 40, 50, 60, 70], 2, 4)
    # range(4, 1, -1) -> 20, 30, 70
    # 1st iteration: i = 4, lst.pop(4) -> [20, 30, 40, 50, 70]
    # 2nd iteration: i = 3, lst.pop(3) -> [20, 30, 40, 70]
    # 3rd iteration: i = 2, lst.pop(2) -> [20, 30, 70]
    for i in range(end_el, start_el - 1, -1):
        lst.pop(i)
    return lst
# Time complexity: O(n^2)
# Space complexity O(1)

print(nth_largest_num([5, 8, 1, 3, 7, 5, 6], 3))
print(remove_range([5, 8, 1, 3, 7, 5, 6,10], 3, 6))