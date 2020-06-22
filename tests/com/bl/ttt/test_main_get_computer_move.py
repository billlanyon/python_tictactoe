from com.bl.ttt.main import get_computer_move


def test_01_main_get_computer_move_random_between_0_and_8():
    get_computer_move()
    assert 0 <= get_computer_move() <= 8
