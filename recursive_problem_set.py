def is_nested_parens(parens):
    # Base case
    if not len(parens):
        return True

    # Recursive case
    # if the parens are not nested, return False
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False

    # if the parens are nested, 
    # return the result of calling is_nested_parens 
    # on the inner parens
    return is_nested_parens(parens[1:-1])