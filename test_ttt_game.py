from ttt_game import Game


def test_01_is_any_row_complete_identifies_complete_row():
    g = Game()
    g.board = [['X', 'X', 'X'],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert g.is_any_row_complete('X')


def test_02_is_any_row_complete_identifies_complete_two_rows():
    g = Game()
    g.board = [['X', 'X', 'X'],
               ['O', 'O', 'O'],
               [' ', ' ', ' ']]
    assert g.is_any_row_complete('O')
    assert g.is_any_row_complete('X')


def test_03_is_any_row_complete_identifies_row():
    g = Game()
    g.board = [['X', 'X', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert not g.is_any_row_complete('X')


def test_04_is_any_row_complete_identifies_complete_column():
    g = Game()
    g.board = [['X', ' ', ' '],
               ['X', ' ', ' '],
               ['X', ' ', ' ']]
    assert not g.is_any_row_complete('X')


def test_05_is_any_row_complete_identifies_complete_back_diagonal():
    g = Game()
    g.board = [['X', ' ', ' '],
               [' ', 'X', ' '],
               [' ', ' ', 'X']]
    assert not g.is_any_row_complete('X')


def test_06_is_any_row_complete_identifies_complete_fwd_diagonal():
    g = Game()
    g.board = [[' ', ' ', 'X'],
               [' ', 'X', ' '],
               ['X', ' ', ' ']]
    assert not g.is_any_row_complete('X')


def test_08_is_any_row_complete_identifies_empty_grid():
    g = Game()
    g.board = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert not g.is_any_row_complete('X')


def test_09_is_any_column_complete_identifies_complete_column():
    g = Game()
    g.board = [['X', ' ', ' '],
               ['X', ' ', ' '],
               ['X', ' ', ' ']]
    assert g.is_any_column_complete('X')


def test_10_is_any_diagonal_complete_identifies_complete_diagonal():
    g = Game()
    g.board = [['X', ' ', ' '],
               [' ', 'X', ' '],
               [' ', ' ', 'X']]
    assert g.is_any_diagonal_complete('X')


def test_11_is_any_row_complete_identifies_complete_row_for_wrong_player():
    g = Game()
    g.board = [['X', 'X', 'X'],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert not g.is_any_row_complete('O')


def test_12_is_any_row_complete_identifies_complete_row_for_symbol_other_than_x_or_o():
    g = Game()
    g.board = [['A', 'A', 'A'],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert not g.is_any_row_complete('O')
