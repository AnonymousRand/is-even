memoize = {}

def is_even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    if n not in memoize:
        memoize[n] = is_even(n - 2)
    return memoize[n]
