def crashing_weights(weights):
    """
    Crashing boxes downwards and combining their weights,
    if a box contains more weight than the box below it.
    """

    # Selecting the box rows.
    bottom_row = weights[-1]
    middle_row = weights[(1)]
    top_row = weights[(0)]

    # checking if toppest box is heavier than middle box.
    # combining weight if that is the case.
    for i in range(len(top_row)):
        if top_row[i] > middle_row[i]:
            middle_row[i] = middle_row[i] + top_row[i]

    # checking if middle box is heavier than bottom box.
    # combining weight if that is the case.            
    for i in range(len(middle_row)):
        if middle_row[i] > bottom_row[i]:
            bottom_row[i] = bottom_row[i] + middle_row[i]

    print(bottom_row)

print("Hello")
print("nononono")



weights = [[1, 3, 0, 2, 2],
           [2, 2, 2, 2, 1],
           [4, 2, 0, 2, 1]]

crashing_weights(weights)