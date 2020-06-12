# Tests make_valid_move()
from com.bl.ttt.tictactoe import Tictactoe


def test_01_make_move_identifies_played_coordinate():
	g = Tictactoe()
	g.player_id = 'O'
	g.cells = ['X', ' ', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	g.make_valid_move('O', 4)
	assert g.cells == ['X', ' ', ' ',
                       ' ', 'O', ' ',
                       ' ', ' ', ' ']


def test_02_make_move_identifies_not_played_coordinate_on_full_board():
	g = Tictactoe()
	g.player_id = 'O'
	g.cells = ['X', 'X', 'O',
			   'O', 'O', 'X',
			   'X', 'O', ' ']
	g.make_valid_move('O', 8)
	assert g.cells == ['X', 'X', 'O',
                       'O', 'O', 'X',
                       'X', 'O', 'O']


def test_03_make_move_identifies_winning_played_coordinate_on_now_full_board():
	g = Tictactoe()
	g.player_id = 'O'
	g.cells = ['X', 'X', 'O',
			   'O', 'O', ' ',
			   'X', 'O', 'X']
	g.make_valid_move('X', 5)
	assert g.cells == ['X', 'X', 'O',
					   'O', 'O', 'X',
					   'X', 'O', 'X']


def test_04_make_move_identifies_not_played_coordinate_on_occupied_cell():
	g = Tictactoe()
	g.player_id = 'O'
	g.cells = ['X', 'X', 'O',
			   'O', ' ', ' ',
			   ' ', ' ', ' ']
	g.make_valid_move('X', 8)
	assert g.cells == ['X', 'X', 'O',
					   'O', ' ', ' ',
					   ' ', ' ', 'X']


def test_05_make_move_identifies_not_played_coordinate_with_invalid_player_id():
	g = Tictactoe()
	g.player_id = 'O'
	g.cells = ['X', 'X', 'O',
			   'O', ' ', ' ',
			   ' ', ' ', ' ']
	g.make_valid_move('X', 7)
	assert g.cells == ['X', 'X', 'O',
					   'O', ' ', ' ',
					   ' ', 'X', ' ']


def test_06_make_move_identifies_not_played_coordinate_with_invalid_coordinate():
	g = Tictactoe()
	g.player_id = 'O'
	g.cells = ['X', 'X', 'O',
			   'O', ' ', ' ',
			   ' ', ' ', ' ']
	g.make_valid_move('O', 6)
	assert g.cells == ['X', 'X', 'O',
					   'O', ' ', ' ',
					   'O', ' ', ' ']
