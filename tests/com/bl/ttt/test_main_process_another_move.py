from unittest import mock
from com.bl.ttt.tictaktoe import process_another_move
from com.bl.ttt.tictactoegame import TictactoeGame


def test_01_main_process_another_move_valid_move():
    g = TictactoeGame()
    g._cells = ['X', 'O', 'X',
               'X', 'O', 'X',
               'O', ' ', 'O']
    g.player1 = 'O'
    g.player2 = 'X'
    g._turn_counter = 10
    with mock.patch('builtins.input', side_effect=[7]):
        process_another_move(g)
        assert g._cells == ['X', 'O', 'X',
                           'X', 'O', 'X',
                           'O', 'X', 'O']
