import random
import matplotlib.pyplot as plt

def generate_cities(num_of_cities, size_of_grid):
    cities = []
    for i in range(num_of_cities):
        cities.append([random.randint(0, size_of_grid), random.randint(0, size_of_grid)])
    return cities


cities = generate_cities(7, 10)
print(cities)


def plot_cities(cities):
    x = [x[0] for x in cities]
    y = [x[1] for x in cities]

    plt.scatter(x, y)
    plt.show()

plot_cities(cities)