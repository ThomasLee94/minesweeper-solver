from game import Game
from board import Board


def test_game_init():
    game = Game(4, 4, 5)

    assert len(game.board.board) == 4
    assert len(game.board.board[0]) == 4
    assert game.width == 4
    assert game.height == 4
    assert game.num_mines == 5

def test_generate_board_on_select():
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)

    assert isinstance(game.board, Board)

def test_generate_board_select():
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)

    assert clicked_tile.is_mine() is False
    assert clicked_tile.is_selected() is True
