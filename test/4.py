import doctest


def square(x):
    '''
    >>> square(2)
    4
    >>> square(4)
    16
    '''
    return x * x


if __name__ == "__main__":
    doctest.testmod(4)
