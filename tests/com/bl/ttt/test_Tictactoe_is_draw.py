from com.bl.ttt.tictactoegame import TictactoeGame


def test_01_is_draw_identifies_draw():
    g = TictactoeGame()
    g._cells = ['X', 'O', 'X',
                'X', 'O', 'X',
                'O', 'X', 'O']
    assert g.is_game_over()


def test_02_is_draw_identifies_not_yet_draw():
    g = TictactoeGame()
    g._cells = ['X', 'O', 'X',
                'X', 'O', ' ',
                'O', 'X', 'O']
    assert not g.is_game_over()


def test_03_is_draw_identifies_win_not_draw():
    g = TictactoeGame()
    g._cells = ['X', 'X', 'O',
                'X', 'O', ' ',
                'O', 'X', 'O']
    assert g._has_won('O')
    assert g.is_game_over()
