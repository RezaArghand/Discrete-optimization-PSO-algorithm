import math


def sigmoid(func):
    result = 1 / (1 + math.exp(-func))
    return result
