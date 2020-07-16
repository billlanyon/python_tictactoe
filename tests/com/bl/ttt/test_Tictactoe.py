# Tests for the Tictactoe class
from com.bl.ttt.tictactoe import Tictactoe


def test_01_cells_list_correct_type():
	t = Tictactoe()
	assert type(t._cells) == list


def test_02_cells_list_correct_length():
	t = Tictactoe()
	assert len(t._cells) == 9


def test_03_repr_check_blank_board():
	t = Tictactoe()
	assert repr(t._cells) == str([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
