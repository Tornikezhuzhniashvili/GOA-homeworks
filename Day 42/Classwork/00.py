def points(games):
    all_points = 0
    for score in games:
        x, y = score.split(":")
        x = int(x)
        y = int(y)
        if x > y:
            all_points += 3 
        elif x == y:
            all_points += 1
    return all_points