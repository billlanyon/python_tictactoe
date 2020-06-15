from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_is_valid_move_identifies_valid_empty_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 2)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert g.is_valid_move(m)


def test_02_is_valid_move_identifies_valid_empty_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 6)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert g.is_valid_move(m)


def test_03_is_valid_move_identifies_invalid_occupied_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 1)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_04_is_valid_move_identifies_invalid_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 9)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_05_is_valid_move_identifies_invalid_coordinate_character():
    g = Tictactoe()
    m = TictactoeMove('J', 2)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_06_is_valid_move_identifies_invalid_negative_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', -4)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_07_is_valid_move_identifies_invalid_none_player_id():
    g = Tictactoe()
    m = TictactoeMove(None, 3)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_08_is_valid_move_identifies_invalid_none_move_cell():
    g = Tictactoe()
    m = TictactoeMove('O', None)
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_09_is_valid_move_identifies_invalid_string_move_cell():
    g = Tictactoe()
    m = TictactoeMove('O', 'Z')
    g.cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_10_is_valid_move_identifies_board_already_complete():
    g = Tictactoe()
    m = TictactoeMove('O', 4)
    g.cells = ['X', 'X', 'O',
               'O', 'O', 'X',
               'X', 'O', 'X']
    assert not g.is_valid_move(m)
