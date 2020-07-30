from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_is_valid_player_default_board_identifies_valid_player():
    g = Tictactoe()
    m = TictactoeMove('O', 2, 0)
    assert g._is_valid_player(m)


def test_02_is_valid_player_default_board_identifies_valid_player():
    g = Tictactoe()
    m = TictactoeMove('X', 0, 2)
    assert g._is_valid_player(m)


def test_03_is_valid_player_default_board_identifies_invalid_player_letter():
    g = Tictactoe()
    m = TictactoeMove('S', 2, 0)
    assert not g._is_valid_player(m)


def test_04_is_valid_player_default_board_identifies_invalid_none_player():
    g = Tictactoe()
    m = TictactoeMove(None, 1, 1)
    assert not g._is_valid_player(m)


def test_05_is_valid_player_default_board_identifies_invalid_int_player():
    g = Tictactoe()
    m = TictactoeMove(4, 2, 0)
    assert not g._is_valid_player(m)
