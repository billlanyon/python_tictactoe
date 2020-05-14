import pytest
from ttt_game import Game


def test_01_horizontal_status_identifies_three_of_a_kind():
    g = Game()
    g.board = [['X', 'X', 'X'],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert g.horizontal_status('X')


def test_02_horizontal_status_identifies_two_of_a_kind():
    g = Game()
    g.board = [['X', 'X', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    assert not g.horizontal_status('X')


def test_03_horizontal_status_identifies_two_of_a_kind():
    g = Game()
    g.board = [['X', ' ', ' '],
               ['X', ' ', ' '],
               ['X', ' ', ' ']]
    assert not g.horizontal_status('X')