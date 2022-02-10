import math
import random


def verify_list_size(theList, maxVariableCount):
    result = []
    if len(theList) > maxVariableCount:
        for i in range(maxVariableCount):
            result.append(theList[i])
    else:
        result = theList
    return result


def initiate_particles_position(minInt, maxInt, maxVariableCount, particleCount):
    a = []
    for i in range(0, particleCount):
        particle = []

        for j in range(0, random.randint(1, maxVariableCount)):
            particle.append(random.randint(minInt, maxInt))
        a.append(particle)
    return a


def initiate_particles_velocity(minInt, maxInt, maxVariableCount, particleCount):
    a = []
    for i in range(0, particleCount):
        particle = []

        for j in range(0, random.randint(1, maxVariableCount)):
            particle.append(random.randint(minInt, maxInt))
        a.append(particle)
    return a


def initiate_best_position(minInt, maxInt, maxVariableCount, particleCount):
    a = []
    for i in range(0, particleCount):
        particle = []

        for j in range(0, random.randint(1, maxVariableCount)):
            particle.append(random.randint(minInt, maxInt))
        a.append(particle)
    return a


def initiate_best_global(minInt, maxInt, maxVariableCount):
    particle = []
    for j in range(0, random.randint(1, maxVariableCount)):
        particle.append(random.randint(minInt, maxInt))
    return particle


# A -B
def minus(firstList, secondList):
    first = []
    for i in firstList:
        # print(i)
        if i in secondList != True:
            a = 0
        else:
            first.append(i)

    return first


# A * B
def multiply(chance, mainList):
    mList = []
    for i in mainList:
        mList.append(i)

    for i in mainList:
        rnd = random.random()

        if rnd > chance:
            mList.remove(i)
    return mList


# A + B
def plus(firstList, secondList):
    result = []
    result.extend(secondList)
    u = minus(firstList, secondList)
    result.extend(u)
    return result


def sigmoid(integer):
    result = 1 / (1 + math.exp(-integer))
    return result

# k = [2, 5, 9, 8, 1, 2, 5]
# h = [2, 3, 9, 5]
# print(initiate_particles_position(-6, 9, 10, 5))
# print(random.randint(-5, 5))
# print(h)
# print(verify_list_size(h, 5))
