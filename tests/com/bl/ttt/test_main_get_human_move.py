from unittest import mock
from com.bl.ttt.tictaktoe import process_another_move
from com.bl.ttt.tictactoegame import TictactoeGame


def test_01_main_get_human_move_valid_move():
    g = TictactoeGame()
    g._cells = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    g.player1 = 'O'
    g.player2 = 'X'
    g._turn_counter = 1
    with mock.patch('builtins.input', side_effect=[0]):
        process_another_move(g)
        assert g._cells == ['O', ' ', ' ',
                           ' ', ' ', ' ',
                           ' ', ' ', ' ']


def test_02_main_get_human_move_valid_move():
    g = TictactoeGame()
    g._cells = ['O', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    g.player1 = 'O'
    g.player2 = 'X'
    g._turn_counter = 2
    with mock.patch('builtins.input', side_effect=[4]):
        process_another_move(g)
        assert g._cells == ['O', ' ', ' ',
                           ' ', 'X', ' ',
                           ' ', ' ', ' ']
