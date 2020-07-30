from com.bl.ttt.tictactoe import TictactoeMove


def test_01_class_tictactoemove_instantiates_with_player_id_x():
	m = TictactoeMove('X', 0, 0)
	assert m.get_player_id() == 'X'


def test_02_class_tictactoemove_instantiates_with_player_id_x():
	m = TictactoeMove('O', 1, 0)
	assert m.get_player_id() == 'O'


def test_03_class_tictactoemove_instantiates_with_move_cell_0_0():
	m = TictactoeMove('X', 0, 1)
	assert m.get_cell_chosen_x() == 0


def test_04_class_tictactoemove_instantiates_with_player_id_y():
	m = TictactoeMove('Y', 0, 2)
	assert m.get_player_id() == 'Y'
