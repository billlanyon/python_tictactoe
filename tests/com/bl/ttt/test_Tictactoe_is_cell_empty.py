from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_is_cell_empty_identifies_empty_cell():
    g = Tictactoe()
    g._cells = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    m = TictactoeMove('O', 0, 1)
    assert g._is_cell_empty(m)


def test_02_is_cell_empty_identifies_empty_cell():
    g = Tictactoe(board_size=3)
    g._cells = [['X', 'X', ' '], [' ', ' ', 'O'], [' ', 'O', ' ']]
    m = TictactoeMove('X', 2, 2)
    assert g._is_cell_empty(m)


def test_03_is_cell_empty_identifies_occupied_cell():
    g = Tictactoe()
    g._cells = [['X', 'X', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    m = TictactoeMove('O', 1, 0)
    assert not g._is_cell_empty(m)


def test_04_is_cell_empty_identifies_empty_string_cell():
    g = Tictactoe()
    g._cells = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']]
    m = TictactoeMove('O', 2, 2)
    assert not g._is_cell_empty(m)
