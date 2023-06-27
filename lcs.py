# Description: Longest Common Subsequence
def lcs(str1, str2, memo=None):
    if not str1 or not str2:
        return 0

    call = (str1, str2)
    if memo is None:
        memo = {}
    elif call in memo:
        return memo[call]

    # split the first character from the rest
    first1, rest1 = str1[0], str1[1:]
    first2, rest2 = str2[0], str2[1:]

    # is this spot a match?
    current_score = 1 if first1 == first2 else 0

    # the result for this position is the max of the current score
    # and each of the maxes from the three possibilities:
    # 1. advance both characters (adding to score if a match)
    # 2. advance only the first character
    # 3. advance only the second character
    result = max(
        current_score + lcs(rest1, rest2, memo),
        lcs(rest1, str2, memo),
        lcs(str1, rest2, memo),
    )

    # store this calculation for later
    memo[call] = result
    # store this calculation for later
    memo[str1][str2] = result

    return result
