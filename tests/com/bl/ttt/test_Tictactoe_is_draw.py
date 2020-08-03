from com.bl.ttt.tictactoe import Tictactoe


def test_01_is_draw_default_board_identifies_draw():
    g = Tictactoe()
    g._cells = [['O', 'X', 'O'], ['X', 'O', 'X'], ['X', 'O', 'X']]
    assert g._is_draw()


def test_02_is_draw_default_board_identifies_not_yet_draw():
    g = Tictactoe()
    g._cells = [['X', 'X', 'O'], ['X', 'O', ' '], ['O', 'O', 'X']]
    assert not g._is_draw()


def test_03_is_draw_default_board_identifies_win_not_draw():
    g = Tictactoe()
    g._cells = [['X', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']]
    assert not g._is_draw()


def test_04_is_draw_seven_board_identifies_win_not_draw():
    g = Tictactoe(board_size=7)
    g._cells = [['O', 'X', 'O', 'O', 'X', 'O', 'X'], ['O', 'X', 'O', 'O', 'X', 'O', 'X'],
                ['O', 'O', 'O', 'O', 'X', 'X', 'O'], ['O', 'X', 'O', 'X', 'X', 'X', 'O'],
                ['X', 'X', 'O', 'X', 'X', 'O', 'X'], ['O', 'X', 'O', 'O', 'X', 'O', 'X'],
                ['O', 'X', 'O', 'O', 'X', 'X', 'O']]
    assert not g._is_draw()
    assert g._has_won('X')


def test_05_is_draw_seven_board_identifies_draw():
    g = Tictactoe(board_size=7)
    g._cells = [['O', 'X', 'O', 'O', 'X', 'O', 'X'], ['O', 'X', 'O', 'O', 'X', 'O', 'X'],
                ['O', 'O', 'O', 'O', 'X', 'X', 'O'], ['O', 'X', 'X', 'X', 'O', 'X', 'O'],
                ['X', 'X', 'O', 'X', 'X', 'O', 'X'], ['O', 'X', 'O', 'O', 'X', 'O', 'X'],
                ['O', 'X', 'O', 'O', 'X', 'X', 'O']]
    assert g._is_draw()
