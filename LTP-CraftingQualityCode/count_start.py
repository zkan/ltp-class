def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.

    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    >>> count_startswith(['test', 'tdd', 'tone'], 't')
    3
    >>> count_startswith(['test', 'tdd', 'tone'], 'x')
    0
    """

    """
    startswith = L[:]

    for item in L:
        if item.startswith(ch):
            startswith.remove(item)

    return len(L) - len(startswith)
    """

    startswith = []

    for item in L:
        if item.startswith(ch):
            startswith.append(item)

    return len(startswith)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

