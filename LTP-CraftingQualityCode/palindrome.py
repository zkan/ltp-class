# Reverse the string. Compare the reversed string to the original string.
def is_palindrome_v1(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """

    return reverse(s) == s


def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''
    
    # For each character in s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev

    return rev


# Split the string into two halves. Reverse the second half.
# Compare the first half to the reversed second half.
def is_palindrome_v2(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """

    # The number of chars in s.
    n = len(s)

    # Compare the first half of s to the reverse of the second half.
    # Omit the middle char of an odd-length string.
    return s[:n // 2] == reverse(s[n - n // 2:])

# Compare the 1st char to the last char.
# Compare the 2nd char to the second last char.
# ...
# Stop when the middle of the string is reached.
def is_palindrome_v3(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    >>> is_palindrome_v3('x')
    True
    >>> is_palindrome_v3('ax')
    False
    >>> is_palindrome_v3('aa')
    True
    """

    """
    i = 0
    j = len(s) - 1
    
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    return j <= i
    """

    """
    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False

    return True
    """

    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True
    """

    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()


