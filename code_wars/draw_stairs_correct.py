def draw_stair(stair_num):
    """Draw one stair with right spacing."""
    result = ""

    result += " " * stair_num + "I\n"
    
    return result


def draw_stairs(stair_num):
    """Draw stairs in one string and substract the last '\n'."""

    list = range(stair_num)
    stairs = ""

    # Making sure if no stairs are requested, no stairs will be built.
    if stair_num == 0:
        print("No stairs are built.")
        exit()

    # Putting all the stairs in one strin.
    for i in range(stair_num):
        stairs += draw_stair(i)

        # Strip \n of the last stair.
        if list[-1] == list[i]:
            stairs = stairs.strip("\n")

    print(stairs)


draw_stairs(5)

