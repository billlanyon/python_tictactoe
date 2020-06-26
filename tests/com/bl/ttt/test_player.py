from com.bl.ttt.player import TictactoeHumanPlayer, TictactoeComputerPlayer


def test_01_tictactoehumanplayer_instatntiate():
    hp = TictactoeHumanPlayer('Y', 2)
    assert hp.player_id == 'Y'
    assert hp.player_number == 2


def test_02_tictactoecomputerplayer_instatntiate():
    cp = TictactoeComputerPlayer('X', 1)
    assert cp.player_id == 'X'
    assert cp.player_number == 1


def test_03_tictactoecomputerplayer_move_random_between_0_and_8():
    cp = TictactoeComputerPlayer('X', 1)
    cp.get_computer_move()
    assert 0 <= cp.get_computer_move() <= 8
