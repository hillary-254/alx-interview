#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0

    operations = 0
    current_h = 1  # Initial H character in the file
    clipboard = 0  # Number of H characters in the clipboard

    while current_h < n:
        if clipboard == 0:
            # Initialize (the first Copy All and Paste)
            clipboard = current_h
            current_h += clipboard
            operations += 2
        elif n - current_h > 0 and (n - current_h) % current_h == 0:
            # Copy All and Paste
            clipboard = current_h
            current_h += clipboard
            operations += 2
        elif clipboard > 0:
            # Paste
            current_h += clipboard
            operations += 1

    return operations
