def grid_map(inp, op):
    res = []
    for sublist in inp:
        sub_res = []
        for item in sublist:
            print(item)
            res_item = op(item) # call op
            sub_res.append(res_item)
        res.append(sub_res)
    print(f"result = {res}")
    return res

num_grid = [[1,2,3,4], [5,6,7,8,9], [0,2,4]]
char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]

result = grid_map(num_grid, lambda x: x * 2)
