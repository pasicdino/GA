import math
import random
import matplotlib.pyplot as plt

def generate_cities(num_of_cities, size_of_grid):
    cities = []
    for i in range(num_of_cities):
        cities.append([random.uniform(0, size_of_grid), random.uniform(0, size_of_grid)])
    return cities

def generate_cities_on_circle(num_of_cities, radius_of_circle):
    cities = []
    for i in range(num_of_cities):
        angle = random.uniform(0, 2*math.pi)
        cities.append([radius_of_circle*math.cos(angle), radius_of_circle*math.sin(angle)])
    return cities

cities = generate_cities(10, 10)
print(cities)

def plot_cities(cities):
    x = [x[0] for x in cities]
    y = [x[1] for x in cities]

    plt.scatter(x, y)
    plt.show()

plot_cities(cities)