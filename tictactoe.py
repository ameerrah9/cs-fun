# A file containing functions for the Tic Tac Toe game
# Space complexity: O(1) because the board is always 3x3
# Time complexity 0(n^2) because the for row in board loop is O(n) and the if "" in row loop is O(n)
#   for i in range(3) loops are O(1) because they are always 3x3
def tic_tac_toe_winner(board):
    """
    INPUT: Tic Tac Toe board (3x3 matrix)
    OUTPUT: Winner
    """

    # If none of these conditions match,
    for row in board:
        # If any space is '' --> Return None for 'game in progress'
        if "" in row:
            return None

    # Determine if any column winners, eliminate 'win' of ''s
    for i in range(3):
        print("column", board[0][i], board[1][i], board[2][i])
        # check if all elements in column are the same
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != "":
            # if so, return the winner
            return board[0][i]

    # Determine if any row winners, eliminate 'win' of ''s
    for i in range(3):
        print("row", board[i][0], board[i][1], board[i][2])
        # check if all elements in row are the same
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != "":
            return board[i][0]

    # Determine if any diagonal winners, eliminate 'win' of ''s
    # Check if top left to bottom right diagonal is all the same
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != "":
        return board[0][0]

    # Check if top right to bottom left diagonal is all the same
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != "":
        return board[0][2]

    # If none of the above conditions are met, return 'tie'
    return "Tie"


def tic_tac_toe_winner(board):
    if not isinstance(board, list) or len(board) != 3:
        raise ValueError("Invalid board format!")

    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for combination in winning_combinations:
        values = [board[row][col] for row, col in combination]

        if all(value == "X" for value in values):
            return "X"

        if all(value == "O" for value in values):
            return "O"

    if all(value != "" for row in board for value in row):
        return "Tie"

    return None
