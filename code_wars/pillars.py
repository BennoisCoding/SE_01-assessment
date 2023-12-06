def distance_pillars(number_pillars, distance_between_pillars, width_pillar):
    """Calculate distance between first and last pillar."""
   
    if number_pillars <= 1:
        distance = 0
    else:
        distance = (number_pillars - 1) * distance_between_pillars + (number_pillars- 2) * width_pillar
    
    print(distance)


distance_pillars(2, 1000, 10)