# Tests for the Tictactoe class
from com.bl.ttt.tictactoe import Tictactoe


def test_01_cells_list_correct_type():
    t = Tictactoe()
    assert type(t._cells) == list


def test_02_default_board_size_cells_list_correct_length():
    t = Tictactoe()
    assert len(t._cells) == 3


def test_03_board_size_four_cells_list_correct_length():
    t = Tictactoe(board_size=4)
    assert len(t._cells) == 4


def test_04_default_board_size_cells_list_correct_empty_content():
    t = Tictactoe()
    assert t._cells == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def test_04_board_size_four_cells_list_correct_empty_content():
    t = Tictactoe(board_size=4)
    assert t._cells == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


def test_05_is_computer_game_is_instantiated():
    t = Tictactoe(is_computer_game=True)
    assert t._is_computer_game is True


def test_06_empty_player_move_log_is_instantiated():
    t = Tictactoe()
    assert t._player_move_log == {'X': [], 'O': []}
