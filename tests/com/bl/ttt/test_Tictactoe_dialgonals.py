# Tests is_any_diagonal_complete
from com.bl.ttt.tictactoe import Tictactoe


def test_01_is_any_diagonal_complete_identifies_complete_diagonal():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   ' ', 'X', ' ',
			   ' ', ' ', 'X']
	assert g.is_any_diagonal_complete('X')


def test_02_player_status_identifies_o_row_win():
	g = Tictactoe()
	g.cells = [' ', ' ', ' ',
			   'O', 'O', 'O',
			   ' ', ' ', ' ']
	assert g.has_won('O')
