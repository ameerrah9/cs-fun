def fibonacci(n):
    if n == 0 or n == 1:
        return n

    n_minus_2 = 0
    n_minus_1 = 1
    current = 2

    while current <= n:
        next_fib = n_minus_2 + n_minus_1

        # shift down
        n_minus_2 = n_minus_1
        n_minus_1 = next_fib

        current += 1

    return n_minus_1


# Time complexity: O(n)
# Space complexity: O(n)
# Fibonacci sequence that uses dynamic programming
# Takes cache as an optional parameter
def fibonacci_dynamic(n, memo=None):
    # base case
    if n == 0 or n == 1:
        return n

    # initialize cache
    memo = memo if memo is not None else {}

    # check cache
    if n in memo:
        # return cached value
        return memo[n]

    # otherwise, calculate and cache the value
    result = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)

    # cache the value and return it
    memo[n] = result
    return result
