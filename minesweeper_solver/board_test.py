from tile import Tile
from board import Board
import pytest
import pprint

def test_board_no_mines():
    board = Board(5, 5)

    assert len(board.board) == 5
    assert len(board.board[0]) == 5 

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            if not isinstance(board.board[i][j], Tile): raise TypeError
            if board.board[i][j].i != i: raise AssertionError
            if board.board[i][j].j != j: raise AssertionError

            if board.board[i][j].is_mine() is not False: raise AssertionError
            if board.board[i][j].is_blank() is not True: raise AssertionError
            if board.board[i][j].num_adjacent_mines != 0: raise AssertionError

def test_board_blanks():
    board = Board(5, 5)

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            # if tile val is 0, assert that it is blank
            if board.board[i][j].num_adjacent_mines == 0:
                if not board.board[i][j].is_blank():
                    raise AssertionError

            # if tile is blank, assert that val is 0
            if board.board[i][j].is_blank():
                if board.board[i][j].num_adjacent_mines != 0:
                    raise AssertionError

            # if tile is not blank, assert that val is great than 0
            else:
                if board.board[i][j].num_adjacent_mines <= 0:
                    raise AssertionError

def test_board_with_mines_counter():
    board = Board(5, 5)
    board.add_mines(5, 1, 1)

    mine_counter = 0

    assert len(board.board) == 5
    assert len(board.board[0]) == 5 

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            if board.board[i][j]._is_mine:
                mine_counter += 1

    assert mine_counter == 5

def test_board_with_mines_adjacent_vals():
    board = Board(5, 5)
    board.add_mines(5, 1, 1)
    test_board = []

    for i in range(len(board.board)):
        tmp = []
        for j in range(len(board.board[i])):
            if board.board[i][j]._is_mine:
                tmp.append("M")
            else:
                tmp.append(str(board.board[i][j].num_adjacent_mines))
        test_board.append(tmp)
    
    pprint.pprint(test_board)

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            if board.board[i][j].num_adjacent_mines > 0:
                adjacent_mines = 0

                for ni, nj in board.get_neighbours(i, j):
                    if board.board[ni][nj]._is_mine:
                        adjacent_mines += 1
                
                if board.board[i][j].num_adjacent_mines != adjacent_mines:
                    raise AssertionError

# [['0', '0', '0', '1', '1'],
#  ['0', '0', '0', '2', 'M'],
#  ['1', '1', '0', '2', 'M'],
#  ['M', '3', '2', '2', '1'],
#  ['2', 'M', 'M', '1', '0']]