# Board Class

```
__init__(self, width, height):
    Initialize self.  See help(type(self)) for accurate signature.
```

Initialises board with set `width` & `height`

```
add_mines(self, num_mines, i, j) -> None:
"""    
Randomly add the number of mines to the board.
"""
```

```
get_neighbours(self, i, j) -> list
```
Returns a all list of all inbounds coorinates of the given `i` & `j`. 

```
increment_adjacents(self, i, j)
"""
increments all adjacents of mines by 1 that are not mines
"""
```