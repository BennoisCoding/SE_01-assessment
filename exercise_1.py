def legal_move(field):
    """Check if the move is a legal move"""
    
    # Check if there are three diamonds of the same color in a row.
    for row in field:
        for cell in row:
            if cell == row[0] and cell == row[1] and cell == row[2]:
                print("\nThe move is legal.")
                quit()

    # Check if there are three diamonds of the same color in a column.
    check_list = []

    for i in range(3):
        for row in field:
            for cell in row[i:(i+1)]:
                check_list.append(cell)
        if check_list.count(check_list[0]) == 3:
            print("The move is legal.")
            quit()
        else:
            check_list.clear()
    
    # If no matching colors were found the move was not legal
    print("The move is not legal.")
    return False


def candy_crush(field):
    """Let the player make a move and determine if it is a legal move."""

    # Printing initial game_field
    for row in field:
        print(row)
    print("\n")

    x_start = 0
    y_start = 0

    # Choose the diamond's coordinates you want to move. 
    while x_start is 0 or y_start is 0:
        y_start = int(input("Pls enter the row coordinate of the diamond you want to move (1-3): "))
        x_start = int(input("Pls enter the column coordinate of the diamond you want to move (1-3): "))

        # Check that the coordindates are valid.
        if x_start not in range(1, 4) or y_start not in range(1, 4):
            x_start = 0
            y_start = 0
            print("You did not choose valid coordinates. Pls try again.")

    direction = ""
    x_end = 0
    y_end = 0

    # Choose the direction in which you want to move the diamond. 
    while x_end is 0 or y_end is 0:
        print("\nPls enter the direction where you want to move the diamond.")
        print("You can only move up, down, left or right and not outside of the game field.\n")
        direction = input("Write 'UP' or 'DOWN' for moving up or down and 'LEFT' or 'RIGHT' for moving left or right: ").upper()

        if direction == "UP":
            y_end += y_start - 1
            x_end = x_start
        elif direction == "DOWN":
            y_end += y_start + 1
            x_end = x_start
        elif direction == "LEFT":
            y_end = y_start
            x_end += x_start - 1
        elif direction == "RIGHT":
            y_end = y_start
            x_end += x_start + 1

        # Check that the direction is valid
        if x_end not in range(1, 4) or y_end not in range(1, 4):
            x_end = 0
            y_end = 0
            print("You did not choose a valid direction. Pls try again.")   

    # Switching positions of the diamonds
    first_diamond = None
    second_diamond = None

    first_diamond = field[y_start - 1][x_start - 1]
    second_diamond = field[y_end - 1][x_end - 1]

    field[y_end - 1][x_end - 1] = first_diamond
    field[y_start - 1][x_start - 1] = second_diamond

    legal_move(field)

    # Printing game_field after move
    for row in field:
        print(row)
    print("\n")


game_field = [[1, 2, 3],
              [4, 4, 5], 
              [5, 3, 4]]


candy_crush(game_field)