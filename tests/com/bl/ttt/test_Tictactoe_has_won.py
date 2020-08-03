from com.bl.ttt.tictactoe import Tictactoe


def test_01_player_status_identifies_default_board_x_row_win():
    g = Tictactoe()
    g._cells = [['X', 'X', 'X'], [' ', 'O', ' '],  [' ', 'O', 'O']]
    assert g._has_won('X')


def test_02_player_status_identifies_default_board_o_diagonal_win():
    g = Tictactoe()
    g._cells = [['O', 'X', 'X'], [' ', 'O', ' '],  [' ', 'X', 'O']]
    assert g._has_won('O')


def test_03_player_status_identifies_default_board_no_x_diagonal_win():
    g = Tictactoe()
    g._cells = [['O', 'X', 'X'], [' ', 'O', ' '],  [' ', 'X', 'O']]
    assert not g._has_won('X')


def test_04_player_status_identifies_default_board_o_board_complete_win():
    g = Tictactoe()
    g._cells = [['O', 'O', 'X'], ['X', 'O', 'X'],  ['X', 'X', 'O']]
    assert g._has_won('O')


def test_05_player_status_identifies_default_board_board_complete_draw():
    g = Tictactoe()
    g._cells = [['O', 'O', 'X'], ['X', 'X', 'O'],  ['O', 'O', 'X']]
    assert not g._has_won('X')


def test_06_player_status_identifies_default_board_no_win_for_symbol_other_than_x_or_o():
    g = Tictactoe()
    g._cells = [['B', 'X', 'X'], [' ', 'B', ' '],  [' ', 'X', 'B']]
    assert not g._has_won('X')


def test_07_player_status_identifies_default_board_no_win_for_empty_grid():
    g = Tictactoe()
    g._cells = [[' ', ' ', ' '], [' ', ' ', ' '],  [' ', ' ', ' ']]
    assert not g._has_won('X')


def test_08_player_status_identifies_four_board_x_row_win():
    g = Tictactoe(board_size=4)
    g._cells = [['X', ' ', ' ', ' '], ['X', ' ', ' ', ' '],  ['X', ' ', ' ', ' '],
                ['X', ' ', ' ', ' ']]
    assert g._has_won('X')


def test_09_player_status_identifies_five_board_x_row_win():
    g = Tictactoe(board_size=5)
    g._cells = [['X', 'X', 'X', 'X', 'X'], [' ', ' ', ' ', ' ', ' '],  [' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    assert g._has_won('X')


def test_10_player_status_identifies_five_board_x_column_win():
    g = Tictactoe(board_size=5)
    g._cells = [['O', 'X', ' ', ' ', 'X'], [' ', 'X', 'O', ' ', ' '],  [' ', 'X', ' ', 'O', ' '],
                [' ', 'X', ' ', ' ', ' '], [' ', 'X', ' ', ' ', ' ']]
    assert g._has_won('X')


def test_11_player_status_identifies_five_board_o_diagonal_win():
    g = Tictactoe(board_size=5)
    g._cells = [['O', 'X', ' ', 'X', 'X'], [' ', 'O', ' ', ' ', ' '],  [' ', ' ', 'O', ' ', ' '],
                [' ', ' ', ' ', 'O', ' '], [' ', ' ', ' ', ' ', 'O']]
    assert g._has_won('O')


def test_11_player_status_identifies_six_board_o_diagonal_win():
    g = Tictactoe(board_size=6)
    g._cells = [['O', 'X', ' ', 'X', 'X', ' '], ['O', 'O', ' ', 'X', 'X', ' '],  ['O', 'X', 'O', 'X', 'X', ' '],
                ['O', 'X', ' ', 'O', 'X', ' '], ['O', 'X', ' ', 'X', 'O', ' '], ['O', 'X', ' ', 'X', 'X', 'O']]
    assert g._has_won('O')


def test_12_player_status_identifies_seven_board_x_vertical_win():
    g = Tictactoe(board_size=7)
    g._cells = [['O', 'X', ' ', 'O', 'X', ' ', ' '], ['O', 'X', 'O', 'O', 'X', ' ', ' '],
                ['O', ' ', 'O', ' ', 'X', ' ', ' '], ['O', 'X', 'O', 'X', 'X', ' ', ' '],
                ['X', 'X', 'O', 'X', 'X', ' ', ' '], ['O', 'X', 'O', 'O', 'X', ' ', ' '],
                ['O', 'X', 'O', 'O', 'X', ' ', ' ']]



def test_13_player_status_identifies_eight_board_o_horizontal_win():
    g = Tictactoe(board_size=8)
    g._cells = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert g._has_won('O')


def test_14_player_status_identifies_nine_board_x_diagonal_win():
    g = Tictactoe(board_size=9)
    g._cells = [['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']]
    assert g._has_won('X')
