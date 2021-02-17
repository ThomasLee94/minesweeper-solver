import random
import numpy as np

#NOTE: Still get index out of bounds error

class GenerateBoard:
    def __init__(self, width, length):
        self.board = [[0 for x in range(width)] for y in range(length)] 
        self.width = width
        self.height = length
        self.ignore_coords = set()
    
    def _is_inbounds(self, y, x):
        return 0 <=  y < self.height and 0 <= y< self.width
    
    def _is_mine(self, y, x):
        return self.board[y][x] == "M"
    
    def add_mines(self, num_mines, user_coordinate):
        """
        Randomly add the number of mines to the board and returns board
        except of the user_coordinate and its adjacents.
        """

        self.add_ignore_coords(user_coordinate)

        while num_mines != 0:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            # don't place a mine on the same spot twice
            if self._is_mine(y,x):
                continue
            if (y,x) not in self.ignore_coords:
                self.board[y][x] = "M"
                self.increment_adjacents(y, x)
                num_mines -= 1
            else:
                continue
        
        return self.board

    def increment_adjacents(self, y, x):
        """
        increments all adjacents of mines by 1
        """

        directions = [
        (y - 1, x), # up
        (y + 1, x), # down
        (y, x - 1), # left
        (y, x + 1), # right
        (y- 1, x - 1), # top_left
        (y - 1, x + 1), # top_right
        (y + 1, x - 1), # bottom_left
        (y + 1, x + 1), # bottom_right
        ]

        for y, x in directions:
            if self._is_inbounds(y, x) and not self._is_mine(y, x):
                self.board[y][x] += 1
    
    def add_ignore_coords(self, user_coordinate):

        y, x = user_coordinate

        directions = [
        (y - 1, x), # up
        (y + 1, x), # down
        (y, x - 1), # left
        (y, x + 1), # right
        (y- 1, x - 1), # top_left
        (y - 1, x + 1), # top_right
        (y + 1, x - 1), # bottom_left
        (y + 1, x + 1), # bottom_right
        ]

        for y, x in directions:
            if self._is_inbounds(y, x):
                self.ignore_coords.add((y, x))



board = GenerateBoard(10, 10)
board.add_mines(5, (1,1))

print(np.matrix(board.board))
print(board.ignore_coords)

