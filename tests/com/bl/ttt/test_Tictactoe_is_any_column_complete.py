from com.bl.ttt.tictactoegame import TictactoeGame


def test_01__is_any_column_complete_identifies_complete():
    g = TictactoeGame()
    g._cells = ['X', ' ', ' ',
               'X', ' ', ' ',
               'X', ' ', ' ']
    assert g._is_any_column_complete('X')


def test_02__is_any_column_complete_identifies_complete_row():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'X',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g._is_any_column_complete('X')


def test_03__is_any_column_complete_identifies_complete_two_columns():
    g = TictactoeGame()
    g._cells = ['X', 'O', ' ',
               'X', 'O', ' ',
               'X', 'O', ' ']
    assert g._is_any_column_complete('X')


def test_04__is_any_column_complete_identifies_column():
    g = TictactoeGame()
    g._cells = ['X', ' ', ' ',
               'X', ' ', ' ',
               ' ', ' ', ' ']
    assert not g._is_any_column_complete('X')


def test_05__is_any_column_complete_identifies_complete_back_diagonal():
    g = TictactoeGame()
    g._cells = ['X', ' ', ' ',
               ' ', 'X', ' ',
               ' ', ' ', 'X']
    assert not g._is_any_column_complete('X')


def test_06__is_any_column_complete_identifies_complete_fwd_diagonal():
    g = TictactoeGame()
    g._cells = [' ', ' ', 'X',
               ' ', 'X', ' ',
               'X', ' ', ' ']
    assert not g._is_any_column_complete('X')


def test_07__is_any_column_complete_identifies_empty_grid():
    g = TictactoeGame()
    g._cells = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g._is_any_column_complete('X')


def test_08__is_any_column_complete_identifies_complete_column_for_wrong_player():
    g = TictactoeGame()
    g._cells = [' ', 'X', ' ',
               ' ', 'X', ' ',
               ' ', 'X', ' ']
    assert not g._is_any_column_complete('O')


def test_09__is_any_column_complete_identifies_complete_column_for_symbol_other_than_x_or_o():
    g = TictactoeGame()
    g._cells = [' ', ' ', 'A',
               ' ', ' ', 'A',
               ' ', ' ', 'A']
    assert not g._is_any_column_complete('O')
