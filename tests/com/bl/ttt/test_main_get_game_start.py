from unittest import mock
from com.bl.ttt.main import get_game_start


def test_01_main_get_game_start_valid_input():
    with mock.patch('builtins.input', side_effect=['y']):
        assert get_game_start() == 'y'


def test_02_main_get_game_start_valid_input():
    with mock.patch('builtins.input', side_effect=['n']):
        assert get_game_start() == 'n'


def test_03_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=['z']):
        assert get_game_start() is None


def test_04_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=[None]):
        assert get_game_start() is None


def test_05_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=['fffff']):
        assert get_game_start() is None


def test_06_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=['123']):
        assert get_game_start() is None
