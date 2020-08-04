from com.bl.ttt.tictactoe import TictactoeMove


def test_01_class_tictactoemove_instantiates_with_player_id_x():
	m = TictactoeMove('X', 0, 1)
	assert m.get_player_id() == 'X'
	assert m.get_cell_chosen_x() == 0
	assert m.get_cell_chosen_y() == 1


def test_02_class_tictactoemove_instantiates_with_player_id_o():
	m = TictactoeMove('O', 0, 1)
	assert m.get_player_id() == 'O'
	assert m.get_cell_chosen_x() == 0
	assert m.get_cell_chosen_y() == 1


def test_03_class_tictactoemove_instantiates_with__str__():
	m = TictactoeMove('X', 2, 2)
	assert m.__str__() == 'X:2:2'


def test_04_class_tictactoemove_instantiates_with_get_cell_chosen():
	m = TictactoeMove('X', 0, 2)
	assert m.get_cell_chosen() == '0:2'
