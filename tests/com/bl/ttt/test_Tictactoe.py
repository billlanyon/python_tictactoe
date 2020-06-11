"""
Tests for the Tictactoe class
"""
from com.bl.ttt.tictactoe import Tictactoe


def test_01_cells_list_correct_type():
	t = Tictactoe()
	assert type(t.cells) == list


def test_02_cells_list_correct_length():
	t = Tictactoe()
	assert len(t.cells) == 9


def test_03_repr_check():
	t = Tictactoe()
	assert repr(t.cells) == str([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])


def test_04_is_any_row_complete_identifies_complete_row():
	g = Tictactoe()
	g.cells = ['X', 'X', 'X',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert g.is_any_row_complete('X')


def test_05_is_any_row_complete_identifies_complete_one_of_two_rows():
	g = Tictactoe()
	g.cells = ['O', 'O', 'O',
			   'X', 'X', 'X',
			   ' ', ' ', ' ']
	assert g.is_any_row_complete('X')


def test_06_is_any_row_complete_identifies_row():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_07_is_any_row_complete_identifies_complete_column():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   'X', ' ', ' ',
			   'X', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_08_is_any_row_complete_identifies_complete_back_diagonal():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   ' ', 'X', ' ',
			   ' ', ' ', 'X']
	assert not g.is_any_row_complete('X')


def test_09_is_any_row_complete_identifies_complete_fwd_diagonal():
	g = Tictactoe()
	g.cells = [' ', ' ', 'X',
			   ' ', 'X', ' ',
			   'X', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_10_is_any_row_complete_identifies_empty_grid():
	g = Tictactoe()
	g.cells = [' ', ' ', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_11_is_any_row_complete_identifies_complete_row_for_wrong_player():
	g = Tictactoe()
	g.cells = ['X', 'X', 'X',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('O')


def test_12_is_any_row_complete_identifies_complete_row_for_symbol_other_than_x_or_o():
	g = Tictactoe()
	g.cells = ['A', 'A', 'A',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('O')


def test_13_is_any_column_complete_identifies_complete():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   'X', ' ', ' ',
			   'X', ' ', ' ']
	assert g.is_any_column_complete('X')


def test_14_is_any_column_complete_identifies_complete_row():
	g = Tictactoe()
	g.cells = ['X', 'X', 'X',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_column_complete('X')


def test_15_is_any_column_complete_identifies_complete_two_columns():
	g = Tictactoe()
	g.cells = ['X', 'O', ' ',
			   'X', 'O', ' ',
			   'X', 'O', ' ']
	assert g.is_any_column_complete('X')


def test_16_is_any_column_complete_identifies_column():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   'X', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_column_complete('X')


def test_17_is_any_column_complete_identifies_complete_back_diagonal():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   ' ', 'X', ' ',
			   ' ', ' ', 'X']
	assert not g.is_any_column_complete('X')


def test_18_is_any_column_complete_identifies_complete_fwd_diagonal():
	g = Tictactoe()
	g.cells = [' ', ' ', 'X',
			   ' ', 'X', ' ',
			   'X', ' ', ' ']
	assert not g.is_any_column_complete('X')


def test_19_is_any_column_complete_identifies_empty_grid():
	g = Tictactoe()
	g.cells = [' ', ' ', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_column_complete('X')


def test_20_is_any_column_complete_identifies_complete_column_for_wrong_player():
	g = Tictactoe()
	g.cells = [' ', 'X', ' ',
			   ' ', 'X', ' ',
			   ' ', 'X', ' ']
	assert not g.is_any_column_complete('O')


def test_21_is_any_column_complete_identifies_complete_column_for_symbol_other_than_x_or_o():
	g = Tictactoe()
	g.cells = [' ', ' ', 'A',
			   ' ', ' ', 'A',
			   ' ', ' ', 'A']
	assert not g.is_any_column_complete('O')


def test_22_is_any_diagonal_complete_identifies_complete_diagonal():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   ' ', 'X', ' ',
			   ' ', ' ', 'X']
	assert g.is_any_diagonal_complete('X')


def test_23_player_status_identifies_o_row_win():
	g = Tictactoe()
	g.cells = [' ', ' ', ' ',
			   'O', 'O', 'O',
			   ' ', ' ', ' ']
	assert g.player_win('O')


def test_24_player_status_identifies_x_column_win():
	g = Tictactoe()
	g.cells = [' ', 'X', ' ',
			   ' ', 'X', ' ',
			   ' ', 'X', ' ']
	assert g.player_win('X')


def test_25_player_status_identifies_o_diagonal_win():
	g = Tictactoe()
	g.cells = ['O', ' ', ' ',
			   ' ', 'O', ' ',
			   ' ', ' ', 'O']
	assert g.player_win('O')


def test_26_player_status_identifies_no_x_diagonal_win():
	g = Tictactoe()
	g.cells = ['O', ' ', ' ',
			   ' ', 'O', ' ',
			   ' ', ' ', 'O']
	assert not g.player_win('X')


def test_27_player_status_identifies_o_board_complete_win():
	g = Tictactoe()
	g.cells = ['O', 'O', 'X',
			   'X', 'O', 'X',
			   'X', 'X', 'O']
	assert g.player_win('O')


def test_28_player_status_identifies_board_complete_draw():
	g = Tictactoe()
	g.cells = ['O', 'O', 'X',
			   'X', 'X', 'O',
			   'O', 'O', 'X']
	assert not g.player_win('X')


def test_29_player_status_identifies_no_win_for_symbol_other_than_x_or_o():
	g = Tictactoe()
	g.cells = ['B', ' ', ' ',
			   ' ', 'B', ' ',
			   ' ', ' ', 'B']
	assert not g.player_win('X')


def test_30_player_status_identifies_no_win_for_empty_grid():
	g = Tictactoe()
	g.cells = [' ', ' ', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.player_win('X')
