from unittest import mock
from com.bl.ttt.tictaktoe import play_another_game


def test_01_main_get_game_start_valid_input():
    with mock.patch('builtins.input', side_effect=['y']):
        assert play_another_game() == 'Y'


def test_02_main_get_game_start_valid_input():
    with mock.patch('builtins.input', side_effect=['n']):
        assert play_another_game() == 'N'


def test_03_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=['z', 'n']):
        assert play_another_game() == 'N'


def test_04_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=[None, 'Y']):
        assert play_another_game() == 'Y'


def test_06_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=[123, 'N']):
        assert play_another_game() == 'N'
