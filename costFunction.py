import math
import functions as func

p = 1000


def fitness_test(position):
    sumVal = 0.0
    crossVal = 1
    dupTester = 0
    sortTester = 0
    testlist = []
    for i in range(len(position)):
        xi = math.floor(position[i])
        sumVal += (xi)
        crossVal = crossVal * (xi)
        testlist.append(math.floor(position[i]))
    if len(testlist) != len(set(testlist)):
        dupTester = 1000

    # using naive method to
    # check sorted list
    flag = 0
    i = 1
    while i < len(testlist):
        if (testlist[i] < testlist[i - 1]):
            flag = 1
        i += 1

    # printing result
    if (not flag):
        sortTester = 0
    else:
        sortTester = 1000
    result = sumVal + abs(crossVal - p) + dupTester + sortTester
    return result


def fitness_lastTry(position):
    if math.floor(position[1]) != 0:
        r = math.floor(position[1]) ** math.floor(position[2])
    else:
        r = 0

    sum1 = math.floor(position[0]) - r + math.floor(position[3]) * math.floor(position[4])

    result = 1 / (1 + abs(sum1))
    return result


def fitness_rasa(position):
    sumVal = 0.0
    crossVal = 1
    for i in range(len(position)):
        xi = math.floor(position[i])
        sumVal += xi
        crossVal = crossVal * xi

    result = abs(1 / (1 + crossVal)) + 100 * abs(sumVal - 500)

    return result
