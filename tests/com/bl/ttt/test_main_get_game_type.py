from unittest import mock
from com.bl.ttt.main import get_game_type


def test_01_main_get_game_type_valid_input_human():
    with mock.patch('builtins.input', side_effect=['h']):
        assert get_game_type() == 'H'


def test_02_main_get_game_type_valid_input_computer():
    with mock.patch('builtins.input', side_effect=['c']):
        assert get_game_type() == 'C'


def test_03_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=['z']):
        assert get_game_type() is None


def test_04_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=[None]):
        assert get_game_type() is None


def test_05_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=['fffff']):
        assert get_game_type() is None


def test_06_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=['123']):
        assert get_game_type() is None
