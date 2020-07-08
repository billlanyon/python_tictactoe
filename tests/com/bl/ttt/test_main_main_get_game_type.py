from unittest import mock
from com.bl.ttt.main import get_game_type


def test_01_main_main_get_game_type_valid_input():
    with mock.patch('builtins.input', side_effect=['c']):
        assert get_game_type() == 'C'


def test_02_main_main_get_game_type_invalid_input():
    with mock.patch('builtins.input', side_effect=['f']):
        assert not get_game_type() == 'C'


def test_04_main_main_get_game_start_invalid_input():
    with mock.patch('builtins.input', side_effect=[None]):
        assert get_game_type() is None
