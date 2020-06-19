from unittest import mock
from com.bl.ttt.main import process_another_move
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_process_another_move_valid_move():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=['X 0']):
        process_another_move(g)
        assert g.cells[0] == 'X'


def test_02_main_process_another_move_valid_move():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=['o 8']):
        process_another_move(g)
        assert g.cells[8] == 'O'


def test_03_main_process_another_move_invalid_player():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=['Q 8']):
        process_another_move(g)
        assert g.cells[8] == ' '


def test_04_main_process_another_move_invalid_cell():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=['Q 9']):
        process_another_move(g)
        assert g.cells[8] == ' '


def test_05_main_process_another_move_win():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=['O 4']):
        g.cells = ['X', ' ', 'O',
                   ' ', ' ', ' ',
                   'O', ' ', 'X']
        process_another_move(g)
        assert g.has_won('O')


def test_06_main_process_another_move_draw():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=['X 1']):
        g.cells = ['X', ' ', 'O',
                   'O', 'O', 'X',
                   'X', 'X', 'O']
        process_another_move(g)
        assert g.is_draw()
