from unittest import mock
from com.bl.ttt.tictaktoe import get_opponent_type


def test_01_main_get_game_type_valid_input_human():
    with mock.patch('builtins.input', side_effect=['h']):
        assert get_opponent_type() == 'H'


def test_02_main_get_game_type_valid_input_computer():
    with mock.patch('builtins.input', side_effect=['c']):
        assert get_opponent_type() == 'C'


def test_03_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=['z', 'C']):
        assert get_opponent_type() == 'C'


def test_04_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=[None, 'H']):
        assert get_opponent_type() == 'H'


def test_06_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=[123, 'C']):
        assert get_opponent_type() == 'C'
