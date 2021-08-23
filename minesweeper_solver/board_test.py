from game_tile import GameTile
from game_board import GameBoard

def test_board_no_mines():
    board = GameBoard(5, 5)

    print(board.game_board)

    assert len(board.game_board) == 5
    assert len(board.game_board[0]) == 5 

    for i in range(len(board.game_board)):
        for j in range(len(board.game_board[i])):
            game_tile = board.game_board[i][j]
            assert isinstance(game_tile, GameTile)
            assert game_tile.i == i
            assert game_tile.j == j

            assert game_tile.is_mine() is False
            assert game_tile.is_blank() is True
            assert game_tile.num_adjacent_mines == 0

def test_board_invisible_tiles():
    board = GameBoard(5, 5)

    invisible_tiles_counter = 5 * 5

    for row in board.game_board:
        for game_tile in row:
            if not game_tile.is_visible():
                invisible_tiles_counter -= 1
    
    assert invisible_tiles_counter == 0

def test_board_blanks():
    board = GameBoard(5, 5)

    for row in board.game_board:
        for game_tile in row:
            # if tile val is 0, assert that it is blank
            if game_tile.num_adjacent_mines == 0:
                assert game_tile.is_blank()

            # if tile is blank, assert that val is 0
            if game_tile.is_blank():
                assert game_tile.num_adjacent_mines == 0

            # if tile is not blank, assert that val is great than 0
            else:
                assert game_tile.num_adjacent_mines >= 0

def test_board_with_mines_counter():
    board = GameBoard(5, 5)
    game_tile = board.game_board[1][1]
    board.add_mines(5, game_tile)

    assert game_tile.is_mine() is False

    mine_counter = 0

    print(board.game_board)
    for row in board.game_board:
        for new_game_tile in row:
            if new_game_tile.is_mine():
                mine_counter += 1

    assert mine_counter == 5

def test_board_with_mines_adjacent_vals():
    board = GameBoard(5, 5)
    game_tile = board.game_board[1][1]
    board.add_mines(5, game_tile)

    for row in board.game_board:
        for game_tile in row:
            if game_tile.num_adjacent_mines > 0:
                adjacent_mines = 0

                for neighbour_tile in board.get_neighbours(game_tile):
                    if neighbour_tile.is_mine():
                        adjacent_mines += 1
            
                assert game_tile.num_adjacent_mines == adjacent_mines