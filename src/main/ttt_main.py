from src.main import ttt_game

# Instantiate the game instance, which gets the initial board setup from the user
game = ttt_game.Game()
# Run the game in a loop
while True:
    game.display()
    current_status = game.status_check()
    if current_status == 'Game not finished':
        game.input_move()
        # Flip players between turns
        if game.player == "X":
            game.player = "O"
        elif game.player == "O":
            game.player = "X"
    else:
        print(current_status)
        break