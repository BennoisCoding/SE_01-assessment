field = [[2, 1, 2, 3],
         [3, 4, 4, 3], 
         [2, 5, 3, 3],
         [3, 7, 6, 1]]

check_list = []

for i in range(4):
    for row in field:
        for cell in row[i:(i+1)]:
            check_list.append(cell)

        if len(check_list) == 3:
            print(check_list)
            if check_list.count(check_list[0]) == 3:
                print("The move is legal.")
                quit()
            else:
                check_list.remove(check_list[0])
    
    check_list.clear()
    

    