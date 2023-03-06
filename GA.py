import random

import individual

cities = [[2.8772042630674854, 0.6755146794164368], [0.7631050888945423, 7.977539609320381], [6.12592833160131, 8.015152032135182], [8.224559943685591, 4.810170116581878], [3.167443707548707, 9.73465466560635], [4.976426000285059, 5.161592573052834], [4.043780744116312, 5.507745524984201], [9.17387079706267, 1.7895321632702943], [1.3088811144982282, 5.532109252200708], [4.842043477648861, 2.2851486712281077]]


#Step 1. Create an initial population of P chromosomes.
#Step 2. Evaluate the fitness of each chromosome.
pop_size = 20
pop = [individual.Individual(cities) for i in range(pop_size)]


#Step 3. Choose P/2 parents from the current population via proportional selection.

#calculate total fitness: 1.0/values is to inverse it as lower values are considered better
total_fitness = sum(1.0/individual.fitness for individual in pop)

#create a list with probabilities, where probabilities inversely relate to the fitness
selection_probabilities = [(1.0/individual.fitness)/total_fitness for individual in pop]

#zip them into one object, contains tuples of individual, fitness
individuals_with_probabilities = list(zip(pop, selection_probabilities))

#sort them s.t. higher fitness is first
individuals_with_probabilities.sort(key=lambda x: x[1], reverse=True)

#select individuals based on probabilities /todo


