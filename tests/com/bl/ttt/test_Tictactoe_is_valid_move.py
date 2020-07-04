from com.bl.ttt.tictactoegame import TictactoeGame, TictactoeMove


def test_01_is_valid_move_identifies_valid_empty_coordinate():
    g = TictactoeGame()
    m = TictactoeMove('O', 2)
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert g.is_valid_move(m)


def test_02_is_valid_move_identifies_valid_empty_coordinate():
    g = TictactoeGame()
    m = TictactoeMove('O', 6)
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert g.is_valid_move(m)


def test_03_is_valid_move_identifies_invalid_occupied_coordinate():
    g = TictactoeGame()
    m = TictactoeMove('O', 1)
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_04_is_valid_move_identifies_invalid_coordinate():
    g = TictactoeGame()
    m = TictactoeMove('O', 9)
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_05_is_valid_move_identifies_invalid_coordinate_character():
    g = TictactoeGame()
    m = TictactoeMove('J', 2)
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_06_is_valid_move_identifies_invalid_negative_coordinate():
    g = TictactoeGame()
    m = TictactoeMove('O', -4)
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_07_is_valid_move_identifies_invalid_none_player_id():
    g = TictactoeGame()
    m = TictactoeMove(None, 3)
    g._cells = ['X', 'X', ' ',
                ' ', ' ', ' ',
                ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_08_is_valid_move_identifies_invalid_none_move_cell():
    g = TictactoeGame()
    m = TictactoeMove('O', None)
    g._cells = ['X', 'X', ' ',
                ' ', ' ', ' ',
                ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_09_is_valid_move_identifies_invalid_string_move_cell():
    g = TictactoeGame()
    m = TictactoeMove('O', 'Z')
    g._cells = ['X', 'X', ' ',
                ' ', ' ', ' ',
                ' ', ' ', ' ']
    assert not g.is_valid_move(m)


def test_10_is_valid_move_identifies_board_already_complete():
    g = TictactoeGame()
    m = TictactoeMove('O', 4)
    g._cells = ['X', 'X', 'O',
                'O', 'O', 'X',
                'X', 'O', 'X']
    assert not g.is_valid_move(m)
