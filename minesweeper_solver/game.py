from game_board import GameBoard

class Game:
    def __init__(self, width, height, num_mines):
        # self.hidden_board = None
        # self.visible_board = None # in visible board use 0,1,2 to show hidden, visible & flagged tiles
        self.board = GameBoard(width, height, num_mines)
        
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.total_selections = 0
        self.mine_selected = False
        
    def __str__(self):
        return f'{str(self.__class__)}'
        
    def display_number_tile(self, tile):
        return tile.num_adjacent_mines
    
    def is_mine(self, tile):
        """
        checks if the hidden_board[i][j] is a mine (not seen by solver)
        """
        return tile.is_mine()
    
    def is_blank(self, tile):
        """
        Checks if [i][j] is a hidden tile on 
        the hidden board (not seen by the solver) 
        """
        return tile.is_blank()


    def play_game(self):
        """
        Starts the game and asks for user input for terminal game. 
        Runs the rest of the game turn based logic.
        """
        while not (self.board.game_won() or self.board.game_lost()):
            # ask user if they want to place flag or select tile
            f_or_s = None
            while f_or_s != 'f' and f_or_s != 's':
                f_or_s = input('Do you want to (f) Flag or (s) Select? ')

            # ask user for coord to select s or f
            # repeat asking until they give valid input
            i = -1
            while i > self.height or i < 0:
                i = input('i? ')
                if i.isdigit():
                    i = int(i)
                else:
                    i = -1

            j = -1
            while j > self.width or j < 0:
                j = input('j? ')
                if j.isdigit():
                    j = int(j)
                else:
                    j = -1
            
            tile = self.board.board[i][j]

            if self.board._is_inbounds(i, j):
                self.board.select(tile)

            # select or flag given coords. if the given coords selected, ask again
            if tile.is_selected():
                print("try again")
            # if the given coords are flagged and the user selected to select, ask again
            elif tile.is_flagged() and f_or_s == 's':
                print('try again')
            elif not self.board._is_inbounds(i, j):
                print('try again')
            # if the user asked to select, select the coords given. 
            elif f_or_s == 's':
                self.board.select(tile)
            # if user asked to flag, flag or deflag the given coords. 
            elif f_or_s == 'f':
                self.board.flag(tile)
            
            self.display_board()
        
        if self.board.game_lost():
            print("You lost")
        else:
            print("You won")
    
    ########################### VISUALISE BOARD ###########################
    def display_number_tile(self, tile):
        """
        Display terminal board function
        """
        num = tile.num_adjacent_mines
        ENDC = '\033[0m'

        colors = [None,
                  '\033[92m',  # 1 green
                  '\033[96m',  # 2 light blue
                  '\033[91m',  # 3 red
                  '\033[95m',  # 4 pink/purple
                  '\033[94m',  # 5 yellow
                  ]
        color = colors[min(num, 5)]
        return f'{color}{num}{ENDC}'
    
    def tile_representation(self, tile):
        """
        Display terminal board function
        """

        if not tile.is_selected() and not tile.is_flagged():
            # block representation of blocked tile
            return '\u2588'

        elif tile.is_flagged():
            # red block to show flag
            return '\033[91m\u2588\033[0m'

        elif tile.is_blank():
            # blank visible tile
            return ' '

        elif tile.is_mine():
            return '\033[91m*\033[0m'
        else:
            # the number on the visible tile
            return self.display_number_tile(tile)
    
    def display_board(self):
        """
        Display terminal board function
        """
        rows = []
        # place indicies/rows to see easily
        # rows.append('  ' + ''.join(map(str, range(self.width))))

        for row in self.board.board:
            row = ""
            for tile in row:
                print(self.tile_representation(tile))
                row += self.tile_representation(tile)
            rows.append(row)
        
        for row in rows:
            print(row)
        print()


def debug(minesweeper):
    """
    Useful debug function
    """
    for r in minesweeper.board.board:
        print(r)

    print()

    for r in minesweeper.board.board:
        print(r)

    print()

    minesweeper.display_board()


if __name__ == '__main__':
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)
    
    debug(game)

    g = game
    g.play_game()

    # print(m)





        

    

