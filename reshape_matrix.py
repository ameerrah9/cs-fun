# Description: Given a matrix and two integers r and c, 
# return a new matrix such that each element of the new matrix is
# placed in an R x C row-major order.
# Time complexity: O(n)
def reshaped_matrix(matrix, r, c):
    # If the number of elements in the matrix is not equal to r * c, return the original matrix
    # create a variable to hold the number of elements in the matrix
    # multiply the number of rows by the number of columns
    num_value = len(matrix) * len(matrix[0])
    
    # create a variable to hold the output matrix
    output_matrix = []
    # create a variable to hold the new row
    # so that we can append it to the output matrix
    new_row = []
    
    # iterate through the matrix
    for row in matrix:
        # iterate through the values in the row
        for value in row:
                # append the value to the new row
                new_row.append(value)
                # if the length of the new row is equal to the number of columns,
                # append the new row to the output matrix
                # and reset the new row
                # otherwise, continue appending values to the new row
                # until the length of the new row is equal to the number of columns
                # so that we can append the new row to the output matrix
                # and reset the new row so it can be used again
                if len(new_row) == c:
                    output_matrix.append(new_row)
                    # reset the new row to an empty list so that we can use it again for the next row
                    new_row = []

    if num_value != r * c:
        return matrix

    return output_matrix

print(reshaped_matrix([[1,2],[3,4]], 1, 4))
# print(reshaped_matrix([[1,2],[3,4],[5,6],[7,8]], 2, 4))