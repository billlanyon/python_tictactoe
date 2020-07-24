from com.bl.ttt.tictactoe import Tictactoe


def test_01__str__identifies_empty_board_output():
    g = Tictactoe()
    assert str(g) == """
    |   |   |   |
    |   |   |   |
    |   |   |   |"""


def test_02__str__identifies_matching_board_output():
    g = Tictactoe()
    g._cells = ['X', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'X']
    assert str(g) == """
    | X |   |   |
    |   | O |   |
    |   | O | X |"""
