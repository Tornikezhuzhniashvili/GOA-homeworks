def two_oldest_ages(ages):
    sorted_age = sorted(ages, reverse=True)
    return [sorted_age[1], sorted_age[0]]