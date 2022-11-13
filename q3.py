import doctest


def sort_helper(data):
    '''
    This function is the recursive sorting operation.
    for each element it recieves it checks whether it is an sortable object or not.
    if it is - it sorts the object and going deep in the object's elements by a recursive call to itself.

    TESTS: 

    >>> sort_helper((1, 5, 4, 3, 2))
    (1, 2, 3, 4, 5)

    >>> sort_helper([1, [1, 1], 2, 5, -1])
    [-1, 1, 2, 5, [1, 1]]

    >>> sort_helper(['a', [1, 1], 1, 'z', 0.0])
    [0.0, 1, 'a', 'z', [1, 1]]

    >>> sort_helper(['a', (5, 4, 'a', 1), 1, 'z', 0.0])
    [0.0, 1, 'a', 'z', (1, 4, 5, 'a')]

    '''

    # dict - sort by keys
    if isinstance(data, dict):
        new_dict = {}
        # sort by str comparison
        data = dict(sorted(data.items(), key=lambda x: str(x)))
        for key, value in data.items():
            # recursively sorting the dict's elements and updating the new one
            new_dict[key] = sort_helper(value)
        return new_dict

    # tuple - sort and handled as a list - returned after convertion to tuple.
    elif isinstance(data, tuple):
        new_tuple = []
        # sorting by str value, if a complex object - giving it a 'high' value of str ('zzzzzz') to make it last.
        data = sorted(data, key=lambda x: 'zzzzzz' if not isinstance(
            x, int | float | str) else str(x))
        for i in data:
            # as above - recursive call. this time appending as we use a list.
            new_tuple.append(sort_helper(i))
        return tuple(new_tuple)

    # list - sort, handle and recursive sorting. returning a new list appended by all elements by the currect order.
    elif isinstance(data, list):
        new_list = []
        # as above - if complex gets a high str value to be last
        data = sorted(data, key=lambda x: 'zzzzzz' if not isinstance(
            x, int | float | str) else str(x))
        for i in data:
            # as above - recursive call and appending by order
            new_list.append(sort_helper(i))
        return new_list

    # set - sort recursively. returned as a list because convering to set destroys any order within it.
    elif isinstance(data, set):
        new_set = []
        # same as above conditions
        data = sorted(data, key=lambda x: 'zzzzzz' if not isinstance(
            x, int | float | str) else str(x))
        for i in data:
            new_set.append(sort_helper(i))
        return new_set

    # a comparable object (string or integer or float) - returned as is.
    else:
        return data


def print_sorted(data):
    '''
    A wrapper function of the sort_helper().
    Check sort_helper docs for deeper information and testing scenarios.

    This function gets a data of sortable type (or basic objects),
    It sorts it by levels - each element of the inner elements - if iterable - is being sorted.
    Any type of element is being valued as it string value.
    for example:
        print_sorted({'c': 1, 'b': (5, 4, 3), 'a': ['9', '8', '7']}) => 
        {'a': ['7', '8', '9'], 'b': (3, 4, 5), 'c': 1}

    TESTS:

    >>> print_sorted({'c': 1, 'b': (5, 4, 3), 'a': ['9', '8', '7']})
    {'a': ['7', '8', '9'], 'b': (3, 4, 5), 'c': 1}

    >>> print_sorted([{'b': (3, 2, 1), 'aa': 'World', 'a': 'Hello'}, (9, 7.5, 1, 0.0), 'First'])
    ['First', {'a': 'Hello', 'aa': 'World', 'b': (1, 2, 3)}, (0.0, 1, 7.5, 9)]
    '''
    print(sort_helper(data))


if __name__ == '__main__':
    doctest.testmod()
