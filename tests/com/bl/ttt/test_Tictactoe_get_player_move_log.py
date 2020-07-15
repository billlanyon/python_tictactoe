from com.bl.ttt.tictactoe import Tictactoe


def test_01_get_player_move_log_gets_default_output():
    g = Tictactoe()
    g.player_move_log = {'X': [2, 4, 7], 'O': [1, 3, 8]}
    assert g.get_player_move_log() == [2, 1, 4, 3, 7, 8]


def test_02_get_player_move_log_gets_x_output():
    g = Tictactoe()
    g.player_move_log = {'X': [4, 2, 7], 'O': [1, 3, 8]}
    assert g.get_player_move_log('X') == [4, 2, 7]


def test_03_get_player_move_log_gets_o_output():
    g = Tictactoe()
    g.player_move_log = {'X': [2, 4, 7], 'O': [0, 1, 6]}
    assert g.get_player_move_log('O') == [0, 1, 6]


def test_04_get_player_move_log_gets_start_output():
    g = Tictactoe()
    g.player_move_log = {'X': [], 'O': []}
    assert g.get_player_move_log() == []


def test_05_get_player_move_log_gets_draw_output():
    g = Tictactoe()
    g.player_move_log = {'X': [0, 2, 3, 5, 7], 'O': [1, 4, 6, 8]}
    assert g.get_player_move_log() == [0, 1, 2, 4, 3, 6, 5, 8, 7]
