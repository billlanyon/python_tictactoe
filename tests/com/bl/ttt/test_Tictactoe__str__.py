from com.bl.ttt.tictactoegame import TictactoeGame, TictactoeMove


def test_01__str__identifies_empty_board_output():
    g = TictactoeGame()
    assert str(g) == """
    |   |   |   |
    |   |   |   |
    |   |   |   |
    """


def test_02__str__identifies_matching_board_output():
    g = TictactoeGame()
    g._cells = ['X', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'X']
    assert str(g) == """
    | X |   |   |
    |   | O |   |
    |   | O | X |
    """
