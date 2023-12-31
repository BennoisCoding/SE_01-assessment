def special_bomb(list_1, list_2):
    """Check if there is a special 'bomb'."""

    # If the indices of the combos intefere they create a special bomb because they create the shape of an 'L' or 'T'.
    # If the middle coordinates are the same a 'Plus' shape was created which does not count as a special bomb.
    for cell in list_1:
        if cell in list_2 and list_1[1] != list_2[1]:
            print("The move was a special bomb.")


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


field = [[1, 1, 2, 3],
         [2, 2, 2, 3], 
         [3, 1, 2, 1],
         [3, 7, 6, 1]]

legal_move(field)