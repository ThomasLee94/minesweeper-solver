from tile import Tile

class GameTile(Tile):
    def __init__(self, coords, num_adjacent_mines=0, is_mine=False):
        super().__init__(
            coords, num_adjacent_mines=num_adjacent_mines, is_mine=is_mine
        )
        
        self._is_visible = False
        self._is_flagged = False
    
    def __repr__(self):
        return f'GameTile(is_mine={self.is_mine()})'

    def is_flagged(self):
        return self._is_flagged

    def is_visible(self):
        return self._is_visible
    
    def make_visible(self):
        self._is_visible = True