def isEven(number):
    if not isinstance(number, int):
        raise ValueError('Expected an integer')

    return (number % 2 == 0)
