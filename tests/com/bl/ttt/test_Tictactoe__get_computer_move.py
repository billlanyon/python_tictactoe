from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove


def test_01__get_computer_move_default_board():
    cg = Tictactoe(is_computer_game=True)
    cg._cells = [['O', 'X', 'X'], ['X', 'O', 'X'], ['X', 'O', ' ']]
    cg._get_computer_move()
    assert cg.get_player_move_log() == ['2:2']


def test_02__get_computer_move_five_board():
    cg = Tictactoe(is_computer_game=True, board_size=5)
    cg._cells = [['O', 'X', 'X', 'O', 'X'], ['X', 'O', 'O', 'X', 'O'], ['O', 'X', 'X', 'O', 'X'],
                 ['O', 'X', 'X', 'O', 'X'], ['O', 'X', 'X', 'O', ' ']]
    cg._get_computer_move()
    assert cg.get_player_move_log() == ['4:4']
