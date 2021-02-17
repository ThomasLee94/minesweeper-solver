class MineSweeper:
    def __init__(self):
        self.board = None
        self.revealed = None

    def reveal(self):
        pass
    
    def generate_board(self, user_coordinate):
        """
        Generate board based on user input,
        create bombs around the coordinate
        that user chooses.
        """

        board = GenerateBoard(10, 10)
        board.add_mines(5, user_coordinate)

