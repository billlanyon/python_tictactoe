from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_is_cell_in_range_default_board_identifies_valid_cell():
    g = Tictactoe()
    m = TictactoeMove('O', 2, 2)
    assert g._is_cell_in_range(m)


def test_02_is_cell_in_range_default_board_identifies_invalid_cell():
    g = Tictactoe()
    m = TictactoeMove('X', 2, 3)
    assert not g._is_cell_in_range(m)


def test_03_is_cell_in_range_default_board_identifies_invalid_cell():
    g = Tictactoe()
    m = TictactoeMove('O', -3, 2)
    assert not g._is_cell_in_range(m)


def test_04_is_cell_in_range_default_seven_board_identifies_valid_cell():
    g = Tictactoe(board_size=7)
    m = TictactoeMove('O', 6, 6)
    assert g._is_cell_in_range(m)


def test_05_is_cell_in_range_default_nine_board_identifies_valid_cell():
    g = Tictactoe(board_size=9)
    m = TictactoeMove('O', 0, 8)
    assert g._is_cell_in_range(m)


def test_06_is_cell_in_range_default_nine_board_identifies_valid_cell():
    g = Tictactoe(board_size=9)
    m = TictactoeMove('O', 0, 10)
    assert not g._is_cell_in_range(m)
