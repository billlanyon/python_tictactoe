# Tests is_valid_move()
from com.bl.ttt.tictactoe import Tictactoe


def test_01_is_valid_move_identifies_invalid_occupied_coordinate():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_valid_move('1')


def test_02_is_valid_move_identifies_valid_empty_coordinate():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert g.is_valid_move('2')


def test_03_is_valid_move_identifies_invalid_coordinate():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_valid_move('9')


def test_04_is_valid_move_identifies_invalid_coordinate_character():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_valid_move('J')


def test_05_is_valid_move_identifies_invalid_negative_coordinate():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_valid_move('-4')


def test_06_is_valid_move_identifies_invalid_none_coordinate():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_valid_move(None)


def test_07_is_valid_move_identifies_invalid_double_coordinate():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_valid_move(9)


def test_08_is_valid_move_identifies_board_already_complete():
	g = Tictactoe()
	g.cells = ['X', 'X', 'O',
			   'O', 'O', 'X',
			   'X', 'O', 'X']
	assert not g.is_valid_move('3')
