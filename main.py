from winner import check_for_winner
from gameboard import Gameboard

# Create a game board

x_spaces = []
o_spaces = []

turn_tracker = 1
is_winner = False

gameboard = Gameboard()

gameboard.show_gameboard()

while not is_winner:

    if turn_tracker % 2 == 0:
        player = "O"
    else:
        player = "X"

    chosen_space = gameboard.choose_space(player, x_spaces, o_spaces)
    gameboard.update_gameboard(chosen_space, player)
    gameboard.show_gameboard()

    is_winner = check_for_winner(x_spaces, o_spaces)

    turn_tracker += 1

print("Thanks for playing!")

# print(x_spaces[0])

# coords[x_spaces[0]] = "X"

# print(coords)

# print(gameboard)

# check_for_winner(x_spaces, o_spaces)
