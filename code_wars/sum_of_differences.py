def sum_of_differences(numbers):
    """
    Sum differences between consecutive pairs
    in descending order.
    """

    # Sort in descending order.
    numbers.sort(reverse=True)

    result = 0

    for i in range(len(numbers)):
        if i + 1 >= len(numbers):
            print(result)
        else:    
            result += numbers[i] - numbers[i+1]
    

list = [2, 1, 10, 8, 16]
sum_of_differences(list)