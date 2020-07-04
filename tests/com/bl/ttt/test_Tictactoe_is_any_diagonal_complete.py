from com.bl.ttt.tictactoegame import TictactoeGame


def test_01__is_any_diagonal_complete_identifies_complete_diagonal():
    g = TictactoeGame()
    g._cells = ['X', ' ', ' ',
               ' ', 'X', ' ',
               ' ', ' ', 'X']
    assert g._is_any_diagonal_complete('X')


def test_02__is_any_diagonal_complete_identifies_complete_diagonal():
    g = TictactoeGame()
    g._cells = ['X', ' ', 'O',
               ' ', 'O', ' ',
               'O', ' ', 'X']
    assert g._is_any_diagonal_complete('O')


def test_03__is_any_diagonal_complete_identifies_incomplete_diagonal():
    g = TictactoeGame()
    g._cells = ['X', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', 'X']
    assert not g._is_any_diagonal_complete('X')
