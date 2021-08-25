from solver import MineSweeperSolver

def test_solver_init():
    solver = MineSweeperSolver(4, 4, 5)

    print(solver.game.board.board)

    assert len(solver.game.board.board) == 4
    assert len(solver.game.board.board[0]) == 4
    assert solver.game.width == 4
    assert solver.game.height == 4
    assert solver.game.num_mines == 5

def test_solver_get_vis_nums():
    solver = MineSweeperSolver(4, 4, 5)
    clicked_tile = solver.board.board[1][1]
    solver.game.board.select(clicked_tile)

    assert solver.get_visible_numbers() == 5
