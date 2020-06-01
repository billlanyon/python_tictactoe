from ttt_game import Game


def test_01_horizontal_three_of_a_kind_identifies_three_of_a_kind():
    g = Game()
    g.board = [['X', 'X', 'X'],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert g.horizontal_three_of_a_kind('X')


def test_02_horizontal_three_of_a_kind_identifies_three_of_a_kind():
    g = Game()
    g.board = [['X', 'X', 'X'],
               ['O', 'O', 'O'],
               [' ', ' ', ' ']]
    assert g.horizontal_three_of_a_kind('O')
    assert g.horizontal_three_of_a_kind('X')


def test_03_horizontal_three_of_a_kind_identifies_two_of_a_kind_is_not_three_of_a_kind():
    g = Game()
    g.board = [['X', 'X', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert not g.horizontal_three_of_a_kind('X')


def test_04_horizontal_three_of_a_kind_identifies_two_of_a_kind():
    g = Game()
    g.board = [['X', ' ', ' '],
               ['X', ' ', ' '],
               ['X', ' ', ' ']]
    assert not g.horizontal_three_of_a_kind('X')


def test_05_horizontal_three_of_a_kind_identifies_two_of_a_kind():
    g = Game()
    g.board = [['X', ' ', ' '],
               ['X', ' ', ' '],
               ['X', ' ', ' ']]
    assert not g.horizontal_three_of_a_kind('X')
