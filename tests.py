def sort_func(x, y):
    if not isinstance(x, int | float | str) and isinstance(y, int | float | str):
        return -1
    elif not isinstance(y, int | float | str) and isinstance(x, int | float | str):
        return 1
    else:
        return str(x) - str(y)


d = set([5, 2, 4, 1, (3, 2, 1)])
print('1' < 'hello!')
