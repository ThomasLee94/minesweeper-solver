from game import MineSweeper
from board import Board
import pytest


def test_game_init():
    game = MineSweeper(4, 4, 5)

    assert game.board is None
    assert game.width == 4
    assert game.height == 4
    assert game.num_mines == 5

def test_generate_board():
    game = MineSweeper(4, 4, 5)
    game.generate_board(1,1)

    print

    if not isinstance(game.board, Board): raise TypeError

