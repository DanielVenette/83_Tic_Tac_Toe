from winner import check_for_winner
from gameboard import Gameboard


def play_game():
    x_spaces = []
    o_spaces = []

    turn_tracker = 1
    is_winner = False

    # Create a game board
    gameboard = Gameboard()
    gameboard.show_gameboard()

    while not is_winner:

        if turn_tracker > 9:
            print("Cat's game!")
            break
        elif turn_tracker % 2 == 0:
            player = "O"
        else:
            player = "X"

        chosen_space = gameboard.choose_space(player, x_spaces, o_spaces)
        gameboard.update_gameboard(chosen_space, player)
        gameboard.show_gameboard()

        is_winner = check_for_winner(x_spaces, o_spaces)

        turn_tracker += 1


keep_playing = True

while(keep_playing):
    play_game()

    while True:
        user_selection = input("Would you like to play again? (Y/N): ")
        if user_selection == "Y" or user_selection == "y":
            keep_playing = True
            break
        elif user_selection == "N" or user_selection == "n":
            keep_playing = False
            break
        else:
            print("Please enter a valid response")

print("Thanks for playing! ")

# print(x_spaces[0])

# coords[x_spaces[0]] = "X"

# print(coords)

# print(gameboard)

# check_for_winner(x_spaces, o_spaces)
