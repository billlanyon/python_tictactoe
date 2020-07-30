from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_is_valid_move_default_board_identifies_valid_empty_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 0, 2)
    g._cells = [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'O', 'X']]
    assert g.is_valid_move(m)


def test_02_is_valid_move_default_board__identifies_invalid_occupied_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 0, 0)
    g._cells = [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'O', 'X']]
    assert not g.is_valid_move(m)


def test_03_is_valid_move_default_board_identifies_invalid_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 3, 2)
    g._cells = [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'O', 'X']]
    assert not g.is_valid_move(m)


def test_04_is_valid_move_default_board_identifies_invalid_coordinate_character():
    g = Tictactoe()
    m = TictactoeMove('J', 2, 2)
    g._cells = [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'O', 'X']]
    assert not g.is_valid_move(m)


def test_05_is_valid_move_default_board_identifies_invalid_negative_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', -2, 2)
    g._cells = [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'O', 'X']]
    assert not g.is_valid_move(m)


def test_06_is_valid_move_default_board_identifies_board_already_complete():
    g = Tictactoe()
    m = TictactoeMove('X', 1, 1)
    g._cells = [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'O', 'O']]
    assert not g.is_valid_move(m)
