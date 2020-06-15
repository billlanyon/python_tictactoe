from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_is_cell_in_range_identifies_valid_cell():
    g = Tictactoe()
    m = TictactoeMove('O', 2)
    assert g._is_cell_in_range(m)


def test_02_is_cell_in_range_identifies_invalid_cell():
    g = Tictactoe()
    m = TictactoeMove('X', 9)
    assert not g._is_cell_in_range(m)


def test_03_is_cell_in_range_identifies_invalid_cell():
    g = Tictactoe()
    m = TictactoeMove('O', -3)
    assert not g._is_cell_in_range(m)
