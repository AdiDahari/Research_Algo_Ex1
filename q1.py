import doctest
import math

"""
This method takes a function and any number of arguments
and execute the function if and only if the arguments' types match the function parameters types.

Each function bears within it a dict of annotations and their types. For example:

def f1(x: int, y: float, z):
    ...
so:
f1.__annotations__ = {
    'x': <class 'int'>,
    'y': <class 'float'>
}

"""


def safe_call(func, *args, **kwargs):
    # Tests
    '''
    >>> safe_call(f1, x=1, y=1.0, z=1)
    'x + y + z = 3.0'

    >>> safe_call(f1, x=0, y=0.0, z='TEST')
    'x + y = 0.0, z = TEST'

    >>> safe_call(f1, x='a', y=0.0, z=1)
    Traceback (most recent call last):
        ...
    Exception: Type Error: expected <class 'int'>, got <class 'str'>

    >>> safe_call(f1, x=1, y=0, z=1)
    Traceback (most recent call last):
        ...
    Exception: Type Error: expected <class 'float'>, got <class 'int'>

    >>> safe_call(f2, name='Adi')
    'Hello Adi!'

    >>> safe_call(f2, name=0.0)
    Traceback (most recent call last):
        ...
    Exception: Type Error: expected <class 'str'>, got <class 'float'>

    >>> safe_call(f2, name=True)
    Traceback (most recent call last):
        ...
    Exception: Type Error: expected <class 'str'>, got <class 'bool'>

    >>> safe_call(f3)
    I am useless!
    >>> safe_call(f3, x=1, y=0.0, z='Zebra', name='Shimi')
    Traceback (most recent call last):
        ...
    TypeError: f3() got an unexpected keyword argument 'x'

    >>> safe_call(math.sqrt, 1)
    1.0
    >>> safe_call(math.sqrt, -2)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    '''
    try:
        annotations = list(func.__annotations__.items())
    except AttributeError:
        return func(*args, **kwargs)

    if annotations:
        if kwargs:
            for param, value in annotations:
                if type(kwargs[param]) is not value:
                    raise Exception(
                        f'Type Error: expected {value}, got {type(kwargs[param])}')
        if args:
            for i in range(len(annotations)):
                if type(args[i]) is not annotations[i][1]:
                    raise Exception(
                        f'Type Error: expected {annotations[i][1]}, got {type(args[i])}')

    return func(*args, **kwargs)


def f1(x: int, y: float, z):
    if not (isinstance(z, int) or isinstance(z, float)):
        if not z.isnumeric():
            return f'x + y = {x + y}, z = {z}'

        z = float(z)

    return f'x + y + z = {x + y + z}'


def f2(name: str):
    return f'Hello {name}!'


def f3():
    print('I am useless!')


if __name__ == '__main__':
    doctest.testmod()

    # Examples:

    print(safe_call(f1, x=1, y=-1.0, z='z'))

    print(safe_call(f1, 1, 2.0, 3))

    try:
        print(safe_call(f1, x=1, y=-1, z='z'))
    except:
        print(f'Expected Exception caught')

    print(safe_call(f2, **{'name': 'Adi'}))
    try:
        print(safe_call(f2, **{'name': True}))
    except:
        print(f'Expected Exception caught')
    try:
        print(safe_call(f3, **{'name': 'Adi'}))
    except:
        print(f'Expected Exception caught')
