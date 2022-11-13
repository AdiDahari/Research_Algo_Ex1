import doctest
from typing import Any


def four_neighbor_function(node: Any) -> list:
    """
    This method retrieves all of given node's neighbors by horizontal and vertical order
    given this matrix: 
       0 1 2
       _ _ _
    0| a b c
    1| d e f
    2| h i j

    the vertical and horizontal neighbors of node e - (1, 1) are:
        i - (2, 1),
        b - (0, 1),
        f - (1, 2),
        d - (1, 0)

    so the returned list will be: [(2, 1), (0, 1), (1, 2), (1, 0)]

    TESTS:

    >>> four_neighbor_function((0, 0))
    [(1, 0), (-1, 0), (0, 1), (0, -1)]

    >>> four_neighbor_function((1, 1))
    [(2, 1), (0, 1), (1, 2), (1, 0)]
    """
    (y, x) = node
    return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]


"""
"""


def BFS(start, end, neighbor_function):
    """
    This method is the BFS - Breadth First Search
    for finding the path from a starting point to a specific destination.

    it contains 2 lists:
        queue = keeps the paths which has been revealed yet.
        visited = keeps all nodes which has been visited yet.

    By iterating through each node visited, all his neighbors are added by the path
    to the current node appended by themselves.

    if the desired node is being visited - the method will return the path from the starting node to it.

    as the method get the neighbor function as a parameter, it is generic and can work with any logically currect 
    neighboring method

    TESTS:

    >>> BFS((0, 0), (0, 0), four_neighbor_function)
    [(0, 0)]

    >>> BFS((0, 0), (0, 1), four_neighbor_function)
    [(0, 0), (0, 1)]

    >>> BFS((0, 0), (2, 2), four_neighbor_function)
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    >>> BFS((2, 2), (0, 0), four_neighbor_function)
    [(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)]

    >>> BFS((0, 2), (2, 0), four_neighbor_function)
    [(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]

    >>> BFS((0, 0), (-2, -2), four_neighbor_function)
    [(0, 0), (-1, 0), (-2, 0), (-2, -1), (-2, -2)]

    """
    queue = [[start]]  # initializing queue of paths
    visited = [start]  # initializing visited array

    # while queue exists - not empty
    while queue:

        # current path - first in queue
        path = queue.pop(0)

        # last node visited
        curr_node = path[-1]

        if curr_node == end:
            # reached the destination
            return path

        for n in neighbor_function(curr_node):
            # for each neighbor:
            if n not in visited:
                # if neighbor's node has not been visited:

                # mark as visited
                visited.append(n)

                # duplicate current path to the neighbor
                updated_path = list(path)

                # add neighbor to updated path
                updated_path.append(n)

                # add updated path with neighbor to queue
                queue.append(updated_path)


if __name__ == '__main__':
    doctest.testmod()
    # Examples:
    print(BFS((0, 0), (0, 0), four_neighbor_function))
    print(BFS((0, 0), (0, 1), four_neighbor_function))
    print(BFS((0, 0), (0, -1), four_neighbor_function))
    print(BFS((0, 0), (2, 2), four_neighbor_function))
    print(BFS((0, 0), (-2, -2), four_neighbor_function))
    print(BFS((0, 0), (10, -2), four_neighbor_function))
