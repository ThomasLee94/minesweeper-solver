import random
from tile import Tile

class Board(Tile):
    def __init__(self, width, height):
        self.board = []
        self.width = width
        self.height = height

        for i in range(height):
            row = []
            for j in range(width):
                row.append(Tile((i,j)))
            self.board.append(row)
    
    def add_mines(self, num_mines, i, j):
        """
        Randomly add the number of mines to the board.
        """

        ignore_tiles = set()
        ignore_tiles.add(id(self.board[i][j])) # add id of tile obj

        for neighbour_tile in self.get_neighbours(i, j):
            ignore_tiles.add(id(neighbour_tile))

        while num_mines != 0:
            ri = random.randint(0, self.height - 1)
            rj = random.randint(0, self.width - 1)
            tile = self.board[ri][rj]
            # dont place a mine in the same spot twice
            if self._is_mine(tile) or id(tile) in ignore_tiles:
                continue
            tile.make_mine()
            self.increment_adjacents(ri, rj)
            num_mines -= 1

    def _is_inbounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width
    
    def _is_mine(self, tile):
        return tile._is_mine is True

    def increment_adjacents(self, i, j):
        """
        increments all adjacents of mines by 1 that are not mines
        """

        for ni, nj in self.get_neighbours(i, j):
            if not self.board[ni][nj].is_mine():
                self.board[ni][nj].num_adjacent_mines += 1
    
    def get_neighbours(self, i, j):
        """
        Returns a list of all inbounds coorinates of the given
        i & j. 
        """

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

        for ni, nj in directions:
            if self._is_inbounds(ni, nj):
                yield ni, nj
    

    
