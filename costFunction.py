import math

p = 1000


def fitness_test(position):
    sumVal = 0.0
    crossVal = 1
    for i in range(len(position)):
        xi = math.floor(position[i])
        sumVal += (xi)
        crossVal = crossVal * (xi)
    result = sumVal + abs(crossVal - p)
    return result
