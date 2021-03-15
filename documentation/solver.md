```
Help on class MineSweeper in module game:

class MineSweeper(builtins.object)
 |  MineSweeper(width, height, num_mines)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, width, height, num_mines)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  display_board(self)
 |  
 |  display_number_tile(self, i, j)
 |      ########################### VISUALISE BOARD ###########################
 |  
 |  flag(self, i, j)
 |  
 |  game_lost(self)
 |  
 |  game_won(self)
 |  
 |  generate_board(self, i, j)
 |      Generate board based on user input,
 |      create bombs around the coordinate
 |      that user chooses.
 |  
 |  is_blank(self, i, j)
 |  
 |  is_flagged(self, i, j)
 |  
 |  is_mine(self, i, j)
 |  
 |  is_selected(self, i, j)
 |  
 |  play_game(self)
 |  
 |  select(self, i, j)
 |      Selects tiles in the visible board if it is selectable, if the tile
 |      is blank recursively select all of its neighbours
 |  
 |  tile_representation(self, i, j)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```