def grid_map(inp, op):
    """A function which maps a function over a list."""

    for row in inp:
        for i, cell in enumerate(row):
            row[i] = op(cell)

    return inp


    

            



num_grid = [[1,2,3,4], [5,6,7,8,9], [0,2,4]]
char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]

result = grid_map(num_grid, lambda x: x * 2)
print(result)
