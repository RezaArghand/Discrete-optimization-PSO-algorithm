# python implementation of particle swarm optimization (PSO)
# minimizing rastrigin and sphere function

import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys
from time import time  # max float
import costFunction as costF
import parameters as Par
import functions as fun
import matplotlib.pyplot as plt

start_time = time()


# -------fitness functions---------

# rastrigin function


def fitness_rastrigin(position):
    fitnessVal = 0.0
    for i in range(len(position)):
        xi = math.floor(position[i])
        fitnessVal += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
    return fitnessVal


# sphere function


def fitness_sphere(position):
    fitnessVal = 0.0
    for i in range(len(position)):
        xi = math.floor(position[i])
        fitnessVal += (xi * xi)
    return fitnessVal


def fitness_test(position):
    result = costF.fitness_rasa(position)
    return result


# -------------------------

# particle class


class Particle:
    def __init__(self, fitness, dim, minx, maxx, seed):
        self.rnd = random.Random(seed)

        # initialize position of the particle with 0.0 value
        self.position = [0.0 for i in range(dim)]

        # initialize velocity of the particle with 0.0 value
        self.velocity = [0.0 for i in range(dim)]

        # initialize best particle position of the particle with 0.0 value
        self.best_part_pos = [0.0 for i in range(dim)]

        # loop dim times to calculate random position and velocity
        # range of position and velocity is [minx, max]
        for i in range(dim):
            self.position[i] = ((maxx - minx) *
                                self.rnd.random() + minx)
            self.velocity[i] = ((maxx - minx) *
                                self.rnd.random() + minx)

        # compute fitness of particle
        self.fitness = fitness(self.position)  # curr fitness

        # initialize best position and fitness of this particle
        self.best_part_pos = copy.copy(self.position)
        self.best_part_fitnessVal = self.fitness  # best fitness


# particle swarm optimization function

fitnessPlot = []
iterPlot = []


def pso(fitness, max_iter, n, dim, minx, maxx, w, c1, c2, satisfaction_fitness):
    rnd = random.Random(0)

    # create n random particles
    swarm = [Particle(fitness, dim, minx, maxx, i) for i in range(n)]

    # compute the value of best_position and best_fitness in swarm
    best_swarm_pos = [0.0 for i in range(dim)]
    best_swarm_fitnessVal = sys.float_info.max  # swarm best

    # computer best particle of swarm and it's fitness
    for i in range(n):  # check each particle
        if swarm[i].fitness < best_swarm_fitnessVal:
            best_swarm_fitnessVal = swarm[i].fitness
            best_swarm_pos = copy.copy(swarm[i].position)

    # main loop of pso

    Iter = 0
    while Iter < max_iter:

        # after every 10 iterations
        # print iteration number and best fitness value so far
        if Iter % 100 == 0 and Iter > 1:
            print("Iter = " + str(Iter) + " best fitness = %.15f" %
                  best_swarm_fitnessVal)
            # print(best_swarm_pos)
            best_Possition = [math.floor(i) for i in best_swarm_pos]
            print(best_Possition)

        for i in range(n):  # process each particle

            # compute new velocity of curr particle
            for k in range(dim):
                r1 = rnd.random()  # randomizations
                r2 = rnd.random()

                swarm[i].velocity[k] = (
                        (w * swarm[i].velocity[k]) +
                        (c1 * r1 * (swarm[i].best_part_pos[k] - swarm[i].position[k])) +
                        (c2 * r2 *
                         (best_swarm_pos[k] - swarm[i].position[k]))
                )

                # if velocity[k] is not in [minx, max]
                if swarm[i].velocity[k] < minx:
                    swarm[i].velocity[k] = minx
                elif swarm[i].velocity[k] > maxx:
                    swarm[i].velocity[k] = maxx
                # then clip it

            # compute new position using new velocity
            for k in range(dim):
                swarm[i].position[k] += swarm[i].velocity[k]

                if swarm[i].position[k] < minx:
                    swarm[i].position[k] = minx * random.random()
                elif swarm[i].position[k] > maxx:
                    swarm[i].position[k] = maxx * random.random()

            # compute fitness of new position
            swarm[i].fitness = fitness(swarm[i].position)

            # is new position a new best for the particle?
            if swarm[i].fitness < swarm[i].best_part_fitnessVal:
                swarm[i].best_part_fitnessVal = swarm[i].fitness
                swarm[i].best_part_pos = copy.copy(swarm[i].position)

            # is new position a new best overall?
            if swarm[i].fitness < best_swarm_fitnessVal:
                best_swarm_fitnessVal = swarm[i].fitness
                best_swarm_pos = copy.copy(swarm[i].position)

        fitnessPlot.append(best_swarm_fitnessVal)
        iterPlot.append(Iter)

        # for-each particle
        Iter += 1
        w = w * wDamp
        if best_swarm_fitnessVal < satisfaction_fitness:
            break
    # end_while
    return best_swarm_pos


# end pso


# ----------------------------
# Driver code for rastrigin function

dim = Par.varNum  # variables count
fitness = fitness_test  # fitness function name
wDamp = Par.damping_rate_W  # inertia damper
xmax = Par.max_of_variable  # max domain
xmin = Par.min_of_variable  # min domain
satisfaction_fitness = Par.satisfaction_cost_number  # satisfaction point
w = Par.W  # inertia
c1 = Par.C1  # cognitive (particle)
c2 = Par.C2  # social (swarm)
num_particles = Par.number_of_particles  # particle count
max_iter = Par.max_iteration_number  # max iteration

print("Setting num_particles = " + str(num_particles))
print("Setting max_iter    = " + str(max_iter))
print("\nStarting PSO algorithm\n")

best_position = pso(fitness, max_iter, num_particles,
                    dim, xmin, xmax, w, c1, c2, satisfaction_fitness)

BestPosition = [best_position[k] for k in range(dim)]
print("\nPSO completed\n")
print("\nBest variables:")
print([math.floor(best_position[k]) for k in range(dim)])
fitnessVal = fitness(best_position)
print("fitness of best variables = " + str(fitnessVal))
end_time = time()
full_time = end_time - start_time
print("The time consumed = " + str(full_time // 60) + " minutes " + str(full_time % 60) + " seconds ")
print()
print()

fig = plt.figure(1)  # identifies the figure
plt.title("cost function", fontsize='16')  # title
plt.plot(iterPlot, fitnessPlot)  # plot the points
plt.xlabel("iteration", fontsize='13')  # adds a label in the x axis
plt.ylabel("cost function", fontsize='13')  # adds a label in the y axis
# plt.legend(('YvsX'), loc='best')  # creates a legend to identify the plot
# plt.savefig('Y_X.png')  # saves the figure in the present directory
plt.grid()  # shows a grid under the plot
plt.show()
