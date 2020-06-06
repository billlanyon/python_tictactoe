"""
Tests for the Tictactoe class
"""
from com.bl.ttt.ttt_game import Tictactoe


def test_01_cells_list_correct_type():
	t = Tictactoe()
	assert type(t.cells) == list


def test_01_cells_list_correct_length():
	t = Tictactoe()
	assert len(t.cells) == 9
