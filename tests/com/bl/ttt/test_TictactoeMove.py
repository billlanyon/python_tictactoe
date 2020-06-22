# Tests for the TictactoeMove class
from com.bl.ttt.tictactoe import TictactoeMove


def test_01_class_tictactoemove_instantiates_with_player_id_x():
	m = TictactoeMove('X', 0)
	assert m.get_player_id() == 'X'


def test_02_class_tictactoemove_instantiates_with_move_cell_0():
	m = TictactoeMove('X', 0)
	assert m.get_cell_chosen() == 0


def test_03_class_tictactoemove_instantiates_with_player_id_y():
	m = TictactoeMove('Y', 0)
	assert m.get_player_id() == 'Y'


def test_04_class_tictactoemove_instantiates_with_move_cell_8():
	m = TictactoeMove('X', 8)
	assert m.get_cell_chosen() == 8


def test_05_class_tictactoemove_instantiates_with_move_cell_8():
	m = TictactoeMove('Y', 8)
	assert m.get_player_id() == 'Y'


def test_06_class_tictactoemove_instantiates_with_move_cell_7():
	m = TictactoeMove('Y', 7)
	assert m.get_cell_chosen() == 7


# return self.player_id
# return self.get_cell_chosen
