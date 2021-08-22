from board import Board

class GameBoard(Board):
    def __init__(self, width, height):
        super.__init__(
            width, height
        )

    def select(self, tile):
        pass

    def flag(self, tile):
        pass

    def game_over(self):
        pass