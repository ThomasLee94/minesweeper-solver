from board import Board

class MineSweeper:
    def __init__(self, width, height, num_mines):
        # self.hidden_board = None
        # self.visible_board = None # in visible board use 0,1,2 to show hidden, visible & flagged tiles
        self.board = None
        
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.total_selections = 0
        self.mine_selected = False
    
    # def __repr__(self):
    #     return f"MineSweeper(board={self.board.board})"
        
    def __str__(self):
        return f'{str(self.__class__)}'
        
    def generate_board(self, i, j):
        """
        Generate board based on user input,
        create bombs around the coordinate
        that user chooses.
        """

        board = Board(self.width, self.height)
        board.add_mines(self.num_mines, i, j)
        self.select(i,j)
        self.board = board
    
    def select(self, i, j):
        '''
        Selects tiles in the visible board if it is selectable, if the tile
        is blank recursively select all of its neighbours
        '''
        if self.board is None:
            self.generate_board(i, j)

        tile = self.board.board[i][j]

        if self.is_selected(tile) or self.is_flagged(tile):
            return

        self.total_selections += 1
        tile.unhide() 
        tile.selected = True

        if tile.is_mine():
            self.mine_selected = True

        # select all neighbours of blank tiles
        if tile.is_blank():
            for ni, nj in self.board.get_neighbours(i,j):
                print(ni,nj)
                self.select(ni, nj)
        
    def is_flagged(self, tile):
        """
        Checks if [i][j] is flagged on the visible board (seen by solver) 
        """
        return tile.flagged is True
    
    def is_selected(self, tile):
        """
        checks if visible_board[i][j] is selected (seen by solver)
        """
        return tile.selected

    def flag(self, i, j):
        """
        Flags/deflags at the given coordinate
        """

        tile = self.board.board[i][j]
        # deflag
        if self.is_flagged(tile):
            tile.flagged = False

        elif not self.is_selected(tile):
            tile.selected = True
    
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
    
    def game_won(self):
        return self.width * self.height - self.num_mines == self.total_selections
    
    def game_lost(self):
        return self.mine_selected

    def play_game(self):
        """
        Starts the game and asks for user input for terminal game. 
        Runs the rest of the game turn based logic.
        """
        while not (self.game_won() or self.game_lost()):
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
            

            if self.board is None:
                self.generate_board(0, 0)
                if self.board._is_inbounds(i, j):
                    self.generate_board(i, j)
                    self.select(i, j)

            tile = self.board.board[i][j]

            # select or flag given coords. if the given coords selected, ask again
            if self.is_selected(tile):
                print("try again")
            # if the given coords are flagged and the user selected to select, ask again
            elif self.is_flagged(tile) and f_or_s == 's':
                print('try again')
            elif not self.board._is_inbounds(i, j):
                print('try again')
            # if the user asked to select, select the coords given. 
            elif f_or_s == 's':
                self.select(i,j)
            # if user asked to flag, flag or deflag the given coords. 
            elif f_or_s == 'f':
                self.flag(i,j)
            
            self.display_board()
        
        if self.game_lost():
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
    
    def tile_representation(self, i, j):
        """
        Display terminal board function
        """

        tile = self.board.board[i][j]

        if not self.is_selected(tile) and not self.is_flagged(tile):
            # block representation of blocked tile
            return '\u2588'

        elif self.is_flagged(tile):
            # red block to show flag
            return '\033[91m\u2588\033[0m'

        elif self.is_blank(tile):
            # blank visible tile
            return ' '

        elif self.is_mine(tile):
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

        for i in range(self.height):
            row = ''
            # row += f'{0} '
            for j in range(self.width):
                row += self.tile_representation(i, j)
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
    minesweeper = MineSweeper(4, 4, 5)
    minesweeper.generate_board(1,1)
    
    debug(minesweeper)

    m = minesweeper
    m.play_game()

    print(m)





        

    

