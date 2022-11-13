# Research_Algo_Ex1

### Q1 - Safe Call - q1.py
  This question is about type-safe function calls
  
  This function recieves an input of:
  
    1. function.
    2. dictionary of arguments.
  the function ensures each argument fits it's annotated parameter.
  
  if not - raises an Exception.
  
  For example: 
  
  f1(x: int, y: float): ...
  
  safe_call(f1, **kwargs) will check each argument given in the dict kwargs to match it parameter's type.
  
  if x is not an int - raises an Exception, 
  
  if y is not a float - raises an Exception.
  
### Q2 - BFS - q2.py
  This question is about BFS - Breadth First Search
  
  It contains 2 functions:
    
    1. BFS implementation which recieves 3 parameters:
    
      a. start node.
      b. destination node.
      c. neighboring function.
      
      it searches breadthly for path from start to destination by a given neighboring function.
      
      
    2. Neighbor function which recieves a node (int, int) and returns it's 4 neighbors by vertical and horizontal order.
      
      For example:
        four_neighbor_function((1, 1)) => [(2, 1), (0, 1), (1, 2), (1, 0)]
        
### Q3 - Deep Sort - q3.py
  This question is about deep sorting of a complex data.
  
  The sorting function is a recursive method which sort all levels of the given structure and prints it's result.
  
  For example:
  
    print_sorted({'c': 1, 'b': (5, 4, 3), 'a': ['9', '8', '7']}) => 
        {'a': ['7', '8', '9'], 'b': (3, 4, 5), 'c': 1}
        
### Q4 - Coding Game solution
  This question is a implementation of a challenge of codingame.com
  
  The challenge: Shadows of the Knight - Episode 1

  The Solution:
  
    import sys
    import math

    # Auto-generated code below aims at helping you parse
    # the standard input according to the problem statement.

    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]
    min_y = min_x = 0
    max_y = h - 1
    max_x = w - 1

    # game loop
    while True:
        bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # the location of the next window Batman should jump to.

        if bomb_dir.find('U') > -1:
            max_y = y0 - 1
        elif bomb_dir.find('D') > -1:
            min_y = y0 + 1
        if bomb_dir.find('L') > -1:
            max_x = x0 - 1
        elif bomb_dir.find('R') > -1:
            min_x = x0 + 1

        y0 = int(min_y + math.ceil((max_y - min_y) / 2))
        x0 = int(min_x + math.ceil((max_x - min_x) / 2))

        print(f'{x0} {y0}')
        
   Link: https://www.codingame.com/replay/671753603
   
   Screenshot: 
    ![codingame com - Shadows of the Knight - Episode 1](https://user-images.githubusercontent.com/71274563/201516449-7a8f1679-44ff-4580-98f1-885ad1af4f74.png)

      
