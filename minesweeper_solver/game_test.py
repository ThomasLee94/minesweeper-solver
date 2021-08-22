from game import MineSweeper
from board import Board
from tile import Tile


def test_game_init():
    game = MineSweeper(4, 4, 5)

    assert game.board is None
    assert game.width == 4
    assert game.height == 4
    assert game.num_mines == 5

def test_generate_board():
    game = MineSweeper(4, 4, 5)
    clicked_tile = Tile((1,1))
    game.generate_board(clicked_tile)

    assert isinstance(game.board, Board)

def test_generate_board_select():
    game = MineSweeper(4, 4, 5)
    clicked_tile = Tile((1,1))
    game.generate_board(clicked_tile)

    assert clicked_tile.is_mine() is False
    assert clicked_tile.is_hidden() is False


