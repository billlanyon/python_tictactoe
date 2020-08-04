from com.bl.ttt.tictactoe import Tictactoe


def test_01__str__identifies_default_board_empty__str__():
    g = Tictactoe()
    assert str(g) == """  0   1   2
0   |   |  
1   |   |  
2   |   |  """


def test_02__str__identifies_matching_default_board_state():
    g = Tictactoe()
    g._cells = [['X', ' ', ' '], [' ', 'O', ' '],  [' ', 'O', 'X']]
    assert str(g) == """  0   1   2
0 X |   |  
1   | O |  
2   | O | X"""
