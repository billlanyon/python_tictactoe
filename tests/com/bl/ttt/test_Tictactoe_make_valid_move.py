# Tests make_valid_move()
from com.bl.ttt.tictactoegame import TictactoeGame, TictactoeMove


def test_01_make_move_identifies_played_coordinate():
    g = TictactoeGame()
    m = TictactoeMove('O', 4)
    g.make_valid_move(m)
    assert g._cells == [' ', ' ', ' ',
                       ' ', 'O', ' ',
                       ' ', ' ', ' ']


def test_02_make_move_identifies_not_played_coordinate_on_full_board():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'O',
               'O', 'O', 'X',
               'X', 'O', ' ']
    m = TictactoeMove('O', 8)
    g.make_valid_move(m)
    assert g._cells == ['X', 'X', 'O',
                       'O', 'O', 'X',
                       'X', 'O', 'O']


def test_03_make_move_identifies_winning_played_coordinate_on_now_full_board():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'O',
               'O', 'O', ' ',
               'X', 'O', 'X']
    m = TictactoeMove('O', 5)
    g.make_valid_move(m)
    assert g._cells == ['X', 'X', 'O',
                       'O', 'O', 'O',
                       'X', 'O', 'X']


def test_04_make_move_identifies_not_played_coordinate_on_occupied_cell():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'O',
               'O', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 8)
    g.make_valid_move(m)
    assert g._cells == ['X', 'X', 'O',
                       'O', ' ', ' ',
                       ' ', ' ', 'O']


def test_05_make_move_identifies_not_played_coordinate_with_invalid_player_id():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'O',
               'O', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('X', 7)
    g.make_valid_move(m)
    assert g._cells == ['X', 'X', 'O',
                       'O', ' ', ' ',
                       ' ', 'X', ' ']


def test_06_make_move_identifies_not_played_coordinate_with_invalid_coordinate():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'O',
               'O', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 6)
    g.make_valid_move(m)
    assert g._cells == ['X', 'X', 'O',
                       'O', ' ', ' ',
                       'O', ' ', ' ']
