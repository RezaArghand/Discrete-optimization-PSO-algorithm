import random

import costFunction as costF
import functions as fun
import parameters as par

print('starting PSO for discrete parameters...')

x = fun.initiate_particles_position(par.min_of_variable, par.max_of_variable, par.number_of_variables,
                                    par.number_of_particles)
v = fun.initiate_particles_velocity(par.min_of_variable, par.max_of_variable, par.number_of_variables,
                                    par.number_of_particles)
pBest = fun.initiate_best_position(par.min_of_variable, par.max_of_variable, par.number_of_variables,
                                   par.number_of_particles)
gBest = fun.initiate_best_global(par.min_of_variable, par.max_of_variable, par.number_of_variables)

iter = 0
while iter <= par.max_iteration_number:

    # print results every 10 iterations
    if iter % 10 == 0 and iter > 1:
        print(" ")
        print(" iteration= " + str(iter))
        print(" best cost function= " + str(costF.rasa_cost_function(gBest)))
        print(" best result= " + str(costF.function_result(gBest)))
        print(" " + str(gBest))

    # iterate each particle
    for i in range(par.number_of_particles):
        r1 = random.random()
        r2 = random.random()
        w = par.W
        # calculate velocity
        f1 = fun.multiply(w, v[i])
        f2 = fun.minus(pBest[i], x[i])
        f3 = fun.minus(gBest, x[i])
        f4 = fun.multiply(r1 * par.C1, f2)
        f5 = fun.multiply(r2 * par.C2, f3)
        f6 = fun.plus(f4, f5)
        fFinal = fun.plus(f1, f6)
        v[i] = fun.verify_list_size(fFinal, par.number_of_variables)

        xNext = fun.plus(x[i], v[i])
        x[i] = fun.verify_list_size(xNext, par.number_of_variables)

        costNext = costF.rasa_cost_function(x[i])
        costGBest = costF.rasa_cost_function(gBest)
        costPBest = costF.rasa_cost_function(pBest[i])
        if costNext < costGBest:
            gBest = x[i]

        if costNext < costPBest:
            pBest[i] = x[i]

    iter = iter + 1
    w = w * par.damping_rate_W

