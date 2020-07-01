from unittest import mock
from com.bl.ttt.main import process_another_move
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_get_human_move_valid_move():
    g = Tictactoe()
    g.cells = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    g.player1 = 'O'
    g.player2 = 'X'
    g.turn_counter = 2
    with mock.patch('builtins.input', side_effect=[0]):
        process_another_move(g)
        assert g.cells == ['O', ' ', ' ',
                           ' ', ' ', ' ',
                           ' ', ' ', ' ']


def test_02_main_get_human_move_valid_move():
    g = Tictactoe()
    g.cells = ['O', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    g.player1 = 'O'
    g.player2 = 'X'
    g.turn_counter = 3
    with mock.patch('builtins.input', side_effect=[4]):
        process_another_move(g)
        assert g.cells == ['O', ' ', ' ',
                           ' ', 'X', ' ',
                           ' ', ' ', ' ']
