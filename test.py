field = [[1, 2, 3],
              [2, 1, 3], 
              [1, 2, 3]]   

check_list = []

for i in range(3):
    for row in field:
        for cell in row[i:(i+1)]:
            check_list.append(cell)

    if check_list.count(check_list[0]) == 3:
        print("yes")
    else:
        check_list.clear()
    

    