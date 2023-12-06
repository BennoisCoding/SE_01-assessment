def crashing_weights(weights):
    
    for i in range(len(weights)-1):
        row1 = weights[i]
        row2 = weights[i+1]
        
        #if (len(row1) != len(row2)): #error
        for j in range(len(row1)):
            if row1[j] > row2[j]:
                row2[j] += row1[j]

    print(weights[-1])


weights = [[1, 3, 0, 2, 2],
           [2, 2, 2, 2, 1],
           [4, 2, 0, 2, 1]]

crashing_weights(weights)


