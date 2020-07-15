# Tests make_valid_move()
from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_process_valid_move_identifies_played_coordinate():
    g = Tictactoe()
    m = TictactoeMove('O', 4)
    g.process_valid_move(m)
    assert g.cells == [' ', ' ', ' ',
                       ' ', 'O', ' ',
                       ' ', ' ', ' ']


def test_02_process_valid_move_identifies_not_played_coordinate_on_full_board():
    g = Tictactoe()
    g.cells = ['X', 'X', 'O',
               'O', 'O', 'X',
               'X', 'O', ' ']
    m = TictactoeMove('O', 8)
    g.process_valid_move(m)
    assert g.cells == ['X', 'X', 'O',
                       'O', 'O', 'X',
                       'X', 'O', 'O']


def test_03_process_valid_move_identifies_winning_played_coordinate_on_now_full_board():
    g = Tictactoe()
    g.cells = ['X', 'X', 'O',
               'O', 'O', ' ',
               'X', 'O', 'X']
    m = TictactoeMove('O', 5)
    g.process_valid_move(m)
    assert g.cells == ['X', 'X', 'O',
                       'O', 'O', 'O',
                       'X', 'O', 'X']


def test_04_process_valid_move_identifies_not_played_coordinate_on_occupied_cell():
    g = Tictactoe()
    g.cells = ['X', 'X', 'O',
               'O', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 8)
    g.process_valid_move(m)
    assert g.cells == ['X', 'X', 'O',
                       'O', ' ', ' ',
                       ' ', ' ', 'O']


def test_05_process_valid_move_identifies_not_played_coordinate_with_invalid_player_id():
    g = Tictactoe()
    g.cells = ['X', 'X', 'O',
               'O', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('X', 7)
    g.process_valid_move(m)
    assert g.cells == ['X', 'X', 'O',
                       'O', ' ', ' ',
                       ' ', 'X', ' ']


def test_06_process_valid_move_identifies_not_played_coordinate_with_invalid_coordinate():
    g = Tictactoe()
    g.cells = ['X', 'X', 'O',
               'O', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 6)
    g.process_valid_move(m)
    assert g.cells == ['X', 'X', 'O',
                       'O', ' ', ' ',
                       'O', ' ', ' ']


def test_07_process_valid_move_appends_coordinate_to_player_move_log():
    g = Tictactoe()
    g.cells = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('X', 0)
    g.process_valid_move(m)
    assert g.get_player_move_log() == (('X', [0]), ('O', []))
