# This function returns values quite fast O(n) time or O(n) space, it also has an error
def get_n(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        memoize[n]
    else:
        memoize[n] = get_n(n - 1, memoize) + get_n(n-2, memoize)
    return memoize[n]

print(get_n(5))