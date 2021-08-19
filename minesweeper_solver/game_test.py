from game import MineSweeper
import pytest
import pprint

def test_game_init():
    minesweeper = MineSweeper(4, 4, 5)

    assert minesweeper.board is None
    assert minesweeper.width == 4
    assert minesweeper.height == 4
    assert minesweeper.num_mines == 5

def test_generate_board():
    minesweeper = MineSweeper(4, 4, 5)
    minesweeper.generate_board(1,1)
    
