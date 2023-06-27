'''
Determine the length of a list recursively without using looping or len()

'''

def len_of_list_recursively(my_list):
		# Base case
    if not my_list:
        return 0

    # Slice off first element
    print(f"Value of rest of list {my_list[1:]}")
    # Store length of remaining elements recursively
    # 1 + 3 = 4
    # pass in [5, 7, 9] so it will return 3
    # count of remaining elements is 3 because 5 is the first element and the rest is 3
    remaining_elem = len_of_list_recursively(my_list[1:])
    print(f"Call to len_of_list_recursively {my_list} returning {remaining_elem}")

    # Recursive Case
    return 1 + remaining_elem

print(len_of_list_recursively([1, 5, 7, 9]))