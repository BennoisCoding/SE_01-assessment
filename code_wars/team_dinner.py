def check_flexibility(available_dates, dates_list):
    """Check the flexibility of the most available days."""

    flexibility_list = []
    
    # Go through the flexiblity of available days each person gave that is also part of the most available day.
    for date in available_dates:
        flexibility = 0
        for row in dates_list:
            if date in row:
                flexibility += len(row)
        flexibility_list.append(flexibility)

    most_flexibility = max(flexibility_list)

    # Check if there are multiple most flexible days. If so, go for the day that happens sooner.
    if flexibility_list.count(most_flexibility) > 1:
        flexibility_indices = [index for (index, item) in enumerate(flexibility_list) if item == most_flexibility]

        return flexibility_indices[0]

    return flexibility_list.index(most_flexibility)


def get_days_from_availability(days_and_availability, availability):
    """Get days that are most available to the team."""

    return [k for k, v in days_and_availability.items() if v == availability]


def team_dinner(available_dates: list[list[int]]):
    """Calculate what day fits everyone best."""

    dict = {}

    for i in range(10):
        num = None
        num = sum(x.count(i) for x in available_dates)
        dict[i] = num

    num_people = len(available_dates)
    if num_people <= 0:
        print("\nThere is no team.\n")
        quit()
    print(f"The number of people is {num_people}.\n")

    most_availability_day = (max(dict, key=dict.get))

    most_availability_days = get_days_from_availability(dict, dict[most_availability_day])
    print(f"The day/s with the most availability is/are Day/s {most_availability_days}.\n")

    # Check if most_availability_day is acceptable.
    if (num_people / 2) <= dict[most_availability_day]:
        print(f"The day/s is/are acceptable.\n")
    else:
        print("There is no date that is acceptable.\n")
        quit()

    # Check if flexibility test is necessary and call function.
    if len(most_availability_days) > 1:

        best_index = 0

        best_index = check_flexibility(most_availability_days, available_dates)
        print(f"The best fitting day is Day {most_availability_days[best_index]}.\n")


dates = [[1, 3, 5], [0, 2, 4], [1, 3, 7], [0, 2, 7], [2, 3, 6], [0]]

team_dinner(dates)