def check_for_winner(x_spaces, o_spaces):
    winner_exists = False

    winning_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    for combination in winning_combinations:
        if all(space in x_spaces for space in combination):
            print("X is the winner")
            winner_exists = True
            break
        if all(space in o_spaces for space in combination):
            print("O is the winner")
            winner_exists = True
            break

    # print(f"X spaces: {x_spaces}")
    # print(f"O spaces: {o_spaces}")

    return winner_exists
