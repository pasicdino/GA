import individual

cities = [[0, 4], [7, 1], [3, 7], [4, 2], [2, 7], [2, 5], [9, 10]]
pop_size = 20

pop = [individual.Individual(cities) for i in range(pop_size)]

for individual in pop:
    print(individual.calculate_fitness())