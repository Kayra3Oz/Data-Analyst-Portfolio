
def calculate_average_from_range(range) -> float:
    #range example: "100-120"
    lower, upper = map(int, range.split("-"))
    average = (upper + lower) / 2
    return average