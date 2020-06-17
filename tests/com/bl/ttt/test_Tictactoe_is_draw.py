from com.bl.ttt.tictactoe import Tictactoe


def test_01_is_draw_identifies_draw():
    g = Tictactoe()
    g.cells = ['X', 'O', 'X',
               'X', 'O', 'X',
               'O', 'X', 'O']
    assert g.is_draw()


def test_02_is_draw_identifies_not_yet_draw():
    g = Tictactoe()
    g.cells = ['X', 'O', 'X',
               'X', 'O', ' ',
               'O', 'X', 'O']
    assert not g.is_draw()