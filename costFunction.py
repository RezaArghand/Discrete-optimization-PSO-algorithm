def rasa_cost_function(particle):
    particleSize = len(particle)

    if particleSize == 1:
        sum = particle[0]

    elif particleSize == 2:
        sum = particle[0] - particle[1]

    elif particleSize == 3:
        if particle[1] == 0:
            r = 0
        else:
            r = particle[1] ** particle[2]

        sum = particle[0] - r

    elif particleSize == 4:
        if particle[1] == 0:
            r = 0
        else:
            r = particle[1] ** particle[2]
        sum = particle[0] - r + particle[3]

    elif particleSize == 5:
        if particle[1] == 0:
            r = 0
        else:
            r = particle[1] ** particle[2]
        sum = particle[0] - r + particle[3] * particle[4]

    else:
        sum = 0
    if sum < 0:
        result = 1000
    else:
        result = 1 / (1 + sum)
    return result


def function_result(particle):
    particleSize = len(particle)

    if particleSize == 1:
        sum = particle[0]

    elif particleSize == 2:
        sum = particle[0] - particle[1]

    elif particleSize == 3:
        if particle[1] == 0:
            r = 0
        else:
            r = particle[1] ** particle[2]

        sum = particle[0] - r

    elif particleSize == 4:
        if particle[1] == 0:
            r = 0
        else:
            r = particle[1] ** particle[2]
        sum = particle[0] - r + particle[3]

    elif particleSize == 5:
        if particle[1] == 0:
            r = 0
        else:
            r = particle[1] ** particle[2]
        sum = particle[0] - r + particle[3] * particle[4]

    else:
        sum = 0

    return sum
