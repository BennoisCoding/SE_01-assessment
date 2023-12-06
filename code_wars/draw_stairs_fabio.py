def draw_one_stair(stair_num, is_last):
    result = ""
    result += " " * stair_num
        # You can replace the line above by using this loop:
        #for i in range(stair_num):
        #   result += " "
    result += "I"
    if (not is_last):
        result += "\n"
    #The else branch is not needed because it would not change the result     
    #else:
    #   result += ""
    return result


def draw_stairs(n):
    result = ""
    
    for i in range(n-1):
        result = result + draw_one_stair(i, False)
        
    result += draw_one_stair(n-1, True)
    return result

# printing is not needed for the exercises, 
# but it can help to figure out what is going on
stairs = draw_stairs(0)
print(stairs)