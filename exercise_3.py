def special_bomb(list_1, list_2):
    """Check if there is a special 'bomb'."""

    # If the indices of the combos intefere they create a special bomb because they create the shape of an 'L' or 'T'.
    # If the middle coordinates are the same a 'Plus' shape was created which does not count as a special bomb.
    for cell in list_1:
        if cell in list_2 and list_1[1] != list_2[1]:
            print("The move was a special bomb.")
            quit()


def legal_move(field):
    """Check if the move is a legal move"""
    
    check_list_row = []
    combo_row = None
    row_combo = False

    # Check if there are three diamonds of the same color in a row.
    for row in field:
        for cell in row:
            if cell == row[0] and cell == row[1] and cell == row[2]:
                print("\nThe move is legal.")
                check_list_row.append(cell)
                combo_row = row
                row_combo = True

                # Get the the field index of the diamonds that create a combo of 3 in a row.
                field_index_combo_row = field.index(combo_row)
                special_chk_list_row = []

                # Add the indices to a list.
                for i in range (3):
                    special_chk_list_row.append([field_index_combo_row, i])

                print(special_chk_list_row)    


    check_list_column = []
    column_combo = False

    for i in range(4):
        for row in field:
            for cell in row[i:(i+1)]:
                check_list_column.append(cell)
                

            if len(check_list_column) == 3:
                if check_list_column.count(check_list_column[0]) == 3:
                    print("\nThe move is legal.")
                    column_combo = True
                    remove_chk = False
                    #quit()
                else:
                    check_list_column.remove(check_list_column[0])
                    remove_chk = True
                
                # Add the field indeces of the diamonds that create a combo of 3 in a column to a list.
                special_chk_list_column = []

                if remove_chk == True:
                    for j in range(1, 4):
                        special_chk_list_column.append([j, i])

                if remove_chk == False:
                    for j in range(3):
                        special_chk_list_column.append([j, i])

    check_list_column.clear()

    # Check if there is a diamond combo in a row and in a column and check if the indices interfere.
    if row_combo == True and column_combo == True:
        special_bomb(special_chk_list_row, special_chk_list_column)
    else:
        quit()
    
    # If no matching colors were found the move was not legal
    print("The move is not legal.")
    return False


def candy_crush(field):
    """Let the player make a move and determine if it is a legal move."""

    # Printing initial game_field
    print("\n")
    for row in field:
        print(row)
    print("\n")

    x_start = 0
    y_start = 0

    # Choose the diamond's coordinates you want to move. 
    while x_start is 0 or y_start is 0:
        y_start = int(input("Pls enter the row coordinate of the diamond you want to move (1-4): "))
        x_start = int(input("Pls enter the column coordinate of the diamond you want to move (1-4): "))

        # Check that the coordindates are valid.
        if x_start not in range(1, 5) or y_start not in range(1, 5):
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
        if x_end not in range(1, 5) or y_end not in range(1, 5):
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


game_field = [[2, 1, 4, 3],
              [4, 4, 4, 5], 
              [2, 5, 4, 4],
              [6, 7, 6, 1]]


candy_crush(game_field)