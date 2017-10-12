"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    # initialize results list
    results = []

    while len(a) > 0 or len(b) > 0:

        # if either lst empty
        if a == []:
            results.append(b.pop(0))
        elif b == []:
            results.append(a.pop(0))

        # compare 1st items in both lst. append lower # to results + rm from original
        elif a[0] < b[0]:
            results.append(a.pop(0))
        else:
            results.append(b.pop(0))

    return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
