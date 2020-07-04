from com.bl.ttt.tictactoegame import TictactoeGame


def test_01_is_game_over_on_win():
    ttt = TictactoeGame(is_computer_opponent=False)
    ttt._cells = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert ttt.is_game_over()


def test_02_is_game_over_on_draw():
    ttt = TictactoeGame(is_computer_opponent=False)
    ttt._cells = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    assert ttt.is_game_over()


def test_03_is_game_over_not_complete():
    ttt = TictactoeGame(is_computer_opponent=False)
    ttt._cells = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert not ttt.is_game_over()
