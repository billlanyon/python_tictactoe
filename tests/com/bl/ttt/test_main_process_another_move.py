from unittest import mock
from com.bl.ttt.main import process_another_move
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_process_another_move_valid_move():
    g = Tictactoe()
    g.cells = ['X', 'O', 'X',
               'X', 'O', 'X',
               'O', ' ', 'O']
    g.player1 = 'O'
    g.player2 = 'X'
    g.turn_counter = 10
    with mock.patch('builtins.input', side_effect=[7]):
        process_another_move(g)
        assert g.cells == ['X', 'O', 'X',
                           'X', 'O', 'X',
                           'O', 'X', 'O']
        assert g.is_draw() is True


def test_02_main_process_another_move_valid_move_has_won():
    g = Tictactoe()
    g.cells = ['X', 'O', 'X',
               'X', 'O', 'X',
               ' ', 'O', 'O']
    g.player1 = 'O'
    g.player2 = 'X'
    g.turn_counter = 10
    with mock.patch('builtins.input', side_effect=[6]):
        process_another_move(g)
        assert g.cells == ['X', 'O', 'X',
                           'X', 'O', 'X',
                           'X', 'O', 'O']
        assert g.has_won('X')
