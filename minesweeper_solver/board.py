import random
from tile import Tile

class Board:
    def __init__(self, width, height):
        self.board = []
        self.width = width
        self.height = height

        for i in range(height):
            row = []
            for j in range(width):
                row.append(Tile((i,j)))
            self.board.append(row)
    
    # def __repr__(self):
    #     return f'Board(board={self.board}, width={self.width}, height={self.height})'
    
    def __str__(self):
        return f'{str(self.__class__)}'
    
    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield self.board[i][j]

    def add_mines(self, num_mines, tile):
        """
        Randomly add the number of mines to the board.
        """

        i = tile.i 
        j = tile.j

        ignore_tiles = set()
        ignore_tiles.add((i,j)) 

        for neighbour_tile in self.get_neighbours(tile):
            ignore_tiles.add((neighbour_tile.i, neighbour_tile.j))

        while num_mines != 0:
            ri = random.randint(0, self.height - 1)
            rj = random.randint(0, self.width - 1)
            new_tile = self.board[ri][rj]
            # dont place a mine in the same spot twice
            if self._is_mine(new_tile) or (new_tile.i, new_tile.j) in ignore_tiles:
                continue
            new_tile.make_mine()
            self.increment_adjacents(new_tile)
            num_mines -= 1

    def _is_inbounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width
    
    def _is_mine(self, tile):
        return tile._is_mine is True

    def increment_adjacents(self, tile):
        i, j = tile.i, tile.j
        """
        increments all adjacents of mines by 1 that are not mines
        """

        for neighbour_tile in self.get_neighbours(tile):
            neighbour_tile.num_adjacent_mines += 1
    
    def get_neighbours(self, tile):
        """
        Returns a list of all inbounds coorinates of the given
        i & j. 
        """

        i,j = tile.i, tile.j
        
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
            if self._is_inbounds(ni,nj):
                yield self.board[ni][nj]
    

    
