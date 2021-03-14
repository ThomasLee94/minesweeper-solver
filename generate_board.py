# utilise the yeetcode problems for the reveal

import random
import numpy as np

class Board:
    def __init__(self, width, height):
        self.board = [[0] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.ignore_coords = set()
    
    def add_mines(self, num_mines):
        """
        Randomly add the number of mines to the board and returns board.
        """
        
        while num_mines != 0:
            i = random.randint(0, self.height - 1)
            j = random.randint(0, self.width - 1)
            # dont place a mine in the same spot twice
            if self._is_mine(i, j):
                continue
            if (i, j) not in self.ignore_coords:
                self.board[i][j] = "M"
                self.increment_adjacents(i, j)
                num_mines -= 1
            else:
                continue

    def _is_inbounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width
    
    def _is_mine(self, i, j):
        return self.board[i][j] == "M"

    def increment_adjacents(self, i, j):
        """
        increments all adjacents of mines by 1
        """

        for i, j in self.get_neighbours:
            if self._is_inbounds(i, j) and not self._is_mine(i, j):
                self.board[i][j] += 1
    
    def get_neighbours(self, i, j):

           directions = [
            (i - 1, j), # up
            (i + 1, j), # down
            (i, j - 1), # left
            (i, j + 1), # right
            (i - 1, j - 1), # top_left
            (i - 1, j + 1), # top_right
            (i + 1, j - 1), # bottom_left
            (i + 1, j + 1), # bottom_right
        ]

        return directions

if __name__ == '__main__':
    board = Board(5, 5)
    board.add_mines(5)
    print(np.matrix(board.board))
