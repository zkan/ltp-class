import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(49)
    1
    >>> num_buses(50)
    1
    >>> num_buses(75)
    2
    >>> num_buses(100)
    2
    >>> num_buses(101)
    3
    """

    return int(math.ceil(n / 50.0))


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0.11])
    (0.11, 0)
    >>> stock_price_summary([-0.5])
    (0, -0.5)
    >>> stock_price_summary([0.03, -0.02])
    (0.03, -0.02)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    sum_of_gains = 0
    sum_of_losses = 0
    for price in price_changes:
        if price >= 0:
            sum_of_gains = sum_of_gains + price
        else:
            sum_of_losses = sum_of_losses + price

    return (sum_of_gains, sum_of_losses)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = []
    >>> swap_k(nums, 0)
    >>> nums
    []
    >>> nums = [1]
    >>> swap_k(nums, 0)
    >>> nums
    [1]
    >>> nums = [1, 2]
    >>> swap_k(nums, 1)
    >>> nums
    [2, 1]
    >>> nums = [1, 2, 3]
    >>> swap_k(nums, 1)
    >>> nums
    [3, 2, 1]
    >>> nums = [1, 2, 3, 4]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3, 4]
    >>> nums = [1, 2, 3, 4]
    >>> swap_k(nums, 1)
    >>> nums
    [4, 2, 3, 1]
    >>> nums = [1, 2, 3, 4]
    >>> swap_k(nums, 2)
    >>> nums
    [3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5]
    >>> swap_k(nums, 1)
    >>> nums
    [5, 2, 3, 4, 1]
    >>> nums = [1, 2, 3, 4, 5]
    >>> swap_k(nums, 2)
    >>> nums
    [4, 5, 3, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 3)
    >>> nums
    [4, 5, 6, 1, 2, 3]
    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_k(nums, 3)
    >>> nums
    [5, 6, 7, 4, 1, 2, 3]
    """
   
    if len(L) > 0 and k > 0:
        tmp_L = L[0:k]
        L[0:k] = L[-k:len(L)]
        L[-k:len(L)] = tmp_L


if __name__ == '__main__':
    import doctest
    doctest.testmod()


