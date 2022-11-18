class Gameboard():

    def __init__(self):
        self.coords = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
        }

    def update_gameboard(self, coordinate, player="X"):
        if (1 <= coordinate <= 9):
            self.coords[coordinate] = player

    def show_gameboard(self):
        print(f"{self.coords[1]} | {self.coords[2]} | {self.coords[3]}\n" \
              f"---------\n" \
              f"{self.coords[4]} | {self.coords[5]} | {self.coords[6]}\n" \
              f"---------\n" \
              f"{self.coords[7]} | {self.coords[8]} | {self.coords[9]}\n"
              )

    def choose_space(self, player, x_spaces, o_spaces):
        player_dict = {
            "X": x_spaces,
            "O": o_spaces
        }
        while True:
            chosen_space = int(input(f"Player '{player}', which space would you like to mark?: "))
            if chosen_space in range(1, 10):
                if chosen_space not in x_spaces and chosen_space not in o_spaces:
                    player_dict[player].append(chosen_space)
                    break
                else:
                    print("That number has already been chosen.  Try again")
            else:
                print("Chose a number between 1 and 9.  Try again.")

        return chosen_space
