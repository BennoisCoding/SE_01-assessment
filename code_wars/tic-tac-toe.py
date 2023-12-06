def start_field_input(field, last_move):
    """Start game by choosing symbol and coordinates."""

    symbol = None

    # Check whose next move it is.
    if last_move == "X":
        symbol = "O"
    elif last_move == "O":
        symbol = "X"

    # Making sure that either "X" or "O" is chosen as a symbol.
    while symbol is None:
        symbol = input("\nPls enter your symbol (X/O): ").upper()
        if symbol not in ["X", "O"]:
            symbol = None
            print("You didn't choose one of the available symbols.")

    row = None
    column = None
    print(f"\nIt is Player {symbol}'s move.")
    
    # Choosing coordinates and making sure that they are in range (1-3).
    while row is None or column is None:
        row = int(input("Pls enter your row coordinates (1-3): "))
        column = int(input("Pls enter your column coordinates (1-3): "))
        if row not in range(1, 4) or column not in range(1, 4):
            row = None
            column = None

    # Checking if the place has already been taking and ending the function
    if field[row - 1][column - 1] != None:
        print("\nAlready used, try again.")
        return field, last_move

    field[row - 1][column - 1] = symbol

    # Calling the updated field to be displayed in the terminal.
    for row in field:
        print(f"\n{row}")
    return field, symbol


def check_winner(field):
    """Checking if a player has won or if it is a draw."""

    symbol = ""

    # Check if there are three in a row.
    if field[0][0] == field[0][1] == field[0][2]:
        symbol = field[0][0]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()
    elif field[1][0] == field[1][1] == field[1][2]:
        symbol = field[1][0]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()
    elif field[2][0] == field[2][1] == field[2][2]:
        symbol = field[2][0]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()

    # Check if there are three in a column.
    elif field[0][0] == field[1][0] == field[2][0]:
        symbol = field[0][0]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()
    elif field[0][1] == field[1][1] == field[2][1]:
        symbol = field[0][1]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()
    elif field[0][1] == field[1][1] == field[2][1]:
        symbol = field[0][1]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()

    # Check if there are three diagonally.
    elif field[0][0] == field[1][1] == field[2][2]:
        symbol = field[0][0]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()
    elif field[2][0] == field[1][1] == field[0][2]:
        symbol = field[2][0]
        if symbol != None:
            print(f"\nPlayer {symbol} has won!")
            quit()

    # Check if it is a draw.
    elif None not in field[0] and None not in field [1] and None not in field[2]:
        print("\nIt is a draw!")
        quit()

    return False


def game ():
    """Play a game of Tic Tac Toe."""

    game_field = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]

    last_move = None

    while not check_winner(game_field):
        game_field, last_move = start_field_input(game_field, last_move)


game()




