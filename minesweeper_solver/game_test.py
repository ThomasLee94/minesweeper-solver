from game import Game
from game_board import GameBoard
from board import Board


def test_game_init():
    game = Game(4, 4, 5)

    assert game.board.game_won() is False
    assert game.board.game_lost() is False

    assert len(game.board.board) == 4
    assert len(game.board.board[0]) == 4
    assert game.width == 4
    assert game.height == 4
    assert game.num_mines == 5

def test_generate_board_on_select():
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)

    assert isinstance(game.board, GameBoard)

def test_generate_board_select():
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)

    assert clicked_tile.is_mine() is False
    assert clicked_tile.is_selected() is True
