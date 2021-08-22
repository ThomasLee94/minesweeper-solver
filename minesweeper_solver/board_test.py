from tile import Tile
from board import Board

def test_board_no_mines():
    board = Board(5, 5)

    assert len(board.board) == 5
    assert len(board.board[0]) == 5 

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            tile = board.board[i][j]
            assert isinstance(tile, Tile)
            assert tile.i == i
            assert tile.j == j

            assert tile.is_mine() is False
            assert tile.is_blank() is True
            assert tile.num_adjacent_mines == 0

def test_board_hidden_tiles():
    board = Board(5, 5)

    hidden_tiles = 5 * 5
    hidden_tiles_counter = 0

    for row in board.board:
        for tile in row:
            if tile.is_hidden():
                hidden_tiles_counter += 1
    
    assert hidden_tiles == hidden_tiles_counter

def test_board_blanks():
    board = Board(5, 5)

    for row in board.board:
        for tile in row:
            # if tile val is 0, assert that it is blank
            if tile.num_adjacent_mines == 0:
                assert tile.is_blank()

            # if tile is blank, assert that val is 0
            if tile.is_blank():
                assert tile.num_adjacent_mines == 0

            # if tile is not blank, assert that val is great than 0
            else:
                assert tile.num_adjacent_mines >= 0

def test_board_with_mines_counter():
    board = Board(5, 5)
    tile = board.board[1][1]
    board.add_mines(5, tile)

    assert len(board.board) == 5
    assert len(board.board[0]) == 5 
    assert tile.is_mine() is False

    mine_counter = 0

    for row in board.board:
        for tile in row:
            if tile.is_mine():
                mine_counter += 1

    assert mine_counter == 5

def test_board_with_mines_adjacent_vals():
    board = Board(5, 5)
    tile = board.board[1][1]
    board.add_mines(5, tile)

    for row in board.board:
        for tile in row:
            if tile.num_adjacent_mines > 0:
                adjacent_mines = 0

                for neighbour_tile in board.get_neighbours(tile):
                    if neighbour_tile.is_mine():
                        adjacent_mines += 1
            
                assert tile.num_adjacent_mines == adjacent_mines