from com.bl.ttt.tictactoe import Tictactoe


def test_01_player_status_identifies_x_column_win():
    g = Tictactoe()
    g._cells = [' ', 'X', ' ',
               ' ', 'X', ' ',
               ' ', 'X', ' ']
    assert g.has_won('X')


def test_02_player_status_identifies_o_diagonal_win():
    g = Tictactoe()
    g._cells = ['O', ' ', ' ',
               ' ', 'O', ' ',
               ' ', ' ', 'O']
    assert g.has_won('O')


def test_03_player_status_identifies_no_x_diagonal_win():
    g = Tictactoe()
    g._cells = ['O', ' ', ' ',
               ' ', 'O', ' ',
               ' ', ' ', 'O']
    assert not g.has_won('X')


def test_04_player_status_identifies_o_board_complete_win():
    g = Tictactoe()
    g._cells = ['O', 'O', 'X',
               'X', 'O', 'X',
               'X', 'X', 'O']
    assert g.has_won('O')


def test_05_player_status_identifies_board_complete_draw():
    g = Tictactoe()
    g._cells = ['O', 'O', 'X',
               'X', 'X', 'O',
               'O', 'O', 'X']
    assert not g.has_won('X')


def test_06_player_status_identifies_no_win_for_symbol_other_than_x_or_o():
    g = Tictactoe()
    g._cells = ['B', ' ', ' ',
               ' ', 'B', ' ',
               ' ', ' ', 'B']
    assert not g.has_won('X')


def test_07_player_status_identifies_no_win_for_empty_grid():
    g = Tictactoe()
    g._cells = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.has_won('X')
