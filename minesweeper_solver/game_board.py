from board import Board
from game_tile import GameTile

class GameBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def add_tiles_to_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(GameTile((i,j)))
            self.board.append(row)

    def select(self, game_tile):
        '''
        Selects given tile if it is selectable, if the tile
        is blank recursively select all of its neighbours
        '''
        if self.is_selected(game_tile) or self.is_flagged(game_tile):
            return

        self.total_selections += 1
        game_tile.unhide() 
        game_tile.selected = True

        if game_tile.is_mine():
            self.mine_selected = True

        # select all neighbours of blank tiles
        if game_tile.is_blank():
            for neighbour_tile in self.board.get_neighbours(game_tile):
                self.select(neighbour_tile)

    def flag(self, game_tile):
        """
        Flags/deflags at the given coordinate
        """
        # deflag
        if self.is_flagged(game_tile):
            game_tile.flagged = False

        elif not self.is_selected(game_tile):
            game_tile.selected = True

    def game_won(self):
        return self.width * self.height - self.num_mines == self.total_selections
    
    def game_lost(self):
        return self.mine_selected

if __name__ == "__main__":
    board = GameBoard(5,5)

    print(board.board)

    
    # GameBoard is a subclass of Boar
    # GameTile is a subclass of Tile

    # Board contains a matrix of Tiles
    # GameBoard contains a matrix of GameTiles