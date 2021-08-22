from tile import Tile

class GameTile(Tile):
    def __init__(self, coords, num_adjacent_bombs=0, is_bomb=False):
        super().__init__(
            coords, num_adjacent_bombs=num_adjacent_bombs, is_bomb=is_bomb
        )
        
        self._is_visible = False
        self._is_flagged = False

    def is_flagged(self):
        return self._is_flagged

    def is_visible(self):
        return self._is_visible
    
    def unhide(self):
        self._is_visible = True