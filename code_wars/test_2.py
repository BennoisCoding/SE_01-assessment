def check_flexibility(available_dates, dates_list):

    flexibility_list = []
    
    # Go through the flexiblity of available days each person gave that is also part of the most available day.
    for date in available_dates:
        flexibility = 0
        for row in dates_list:
            if date in row:
                flexibility += len(row)
        flexibility_list.append(flexibility)

    most_flexibility = max(flexibility_list)

    # Check if there are more most flexible days. If so, go for the day that happens sooner.
    if flexibility_list.count(most_flexibility) > 1:
        flexibility_indices = [index for (index, item) in enumerate(flexibility_list) if item == most_flexibility]
        
        print(flexibility_indices[0])

        return flexibility_indices[0]


    return flexibility_list.index(most_flexibility)


def get_days_from_availability(days_and_availability, availability):

    return [k for k, v in days_and_availability.items() if v == availability]




dates = [ [0, 1, 2, 3], [0, 1], [0, 5], [1, 6] ]

dict = {}

for i in range(10):
    num = None
    num = sum(x.count(i) for x in dates)
    dict[i] = num

print(dict)

num_people = len(dates)
print(f"The number of people is {num_people}.\n")

most_availability_day = (max(dict, key=dict.get))

most_availability_days = get_days_from_availability(dict, dict[most_availability_day])
print(f"The days with the most availability are {most_availability_days}.")

# Check if most_availability_day is acceptable.
if (num_people / 2) <= dict[most_availability_day]:
    print(f"The days are acceptable.")
else:
    print("There is no date that is acceptable.")

# Check if flexibility test is necessary and call function.
if len(most_availability_days) > 1:

    best_index = 0

    best_index = check_flexibility(most_availability_days, dates)

    print(f"The best fitting day is Day {most_availability_days[best_index]}.")

    #most_availability_days = check_flexibility()



