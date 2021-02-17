# Solver 
# write an algo that picks a 100% safe box with given info, and store mines that 
# adding more bombs & grids makes it more difficult

# avoid bombs in the coordinate that the user chooses
 

class MineSweeperSolver:
    def __init__(self):
        self.partial_board = None
    
    def fill_board(self):
        """
        This will fill the board with all known
        information
        """
