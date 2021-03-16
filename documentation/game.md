# Game Class



```python
def flag(self, i, j):
    """
    Flags/deflags at the given coordinate
    """
```
```python
def game_lost(self) -> bool:
```

```python
def game_won(self) -> bool:
```

```python
def generate_board(self, i, j) -> None:
    """
    Generate board based on user input,
    create bombs around the coordinate
    that user chooses.
    """
```

```python
def is_blank(self, i, j) -> bool:
    """
    Checks if [i][j] is a hidden tile on 
    the hidden board (not seen by the solver) 
    """
```

```python
def is_flagged(self, i, j) -> bool:
    """
    Checks if [i][j] is flagged on the visible board (seen by solver) 
    """
```

```python
def is_mine(self, i, j) -> bool:
    """
    checks if the hidden_board[i][j] is a mine (not seen by solver)
    """
```

```python
def is_selected(self, i, j) -> bool:
    """
    checks if visible_board[i][j] is selected (seen by solver)
    """
```

```python
def play_game(self):
    """
    Starts the game and asks for user input for terminal game. 
    Runs the rest of the game turn based logic.
    """
```

```python
def select(self, i, j)
    Selects tiles in the visible board if it is selectable, if the tile
    is blank recursively select all of its neighbours
```

## Board visualisation in terminal

```python
########################### VISUALISE BOARD ###########################
def display_board(self):

def display_number_tile(self, i, j):

def tile_representation(self, i, j):
```