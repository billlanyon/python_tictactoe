from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01_process_valid_move_default_board_identifies_played_coordinate():
    g = Tictactoe()
    g._cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    m = TictactoeMove('X', 0, 2)
    g.process_valid_move(m)
    assert g._player_move_log['X'] == ['0:2']


def test_02_process_valid_move_default_board_identifies_not_played_coordinate():
    g = Tictactoe()
    g._cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    m = TictactoeMove('O', 0, 2)
    g.process_valid_move(m)
    assert g._cells == [[' ', ' ', ' '], [' ', ' ', ' '], ['O', ' ', ' ']]
