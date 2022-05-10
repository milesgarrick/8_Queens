import numpy as np
import random


# Holds a puzzle state and fitness
class Chromosome:
    def __init__(self, new_state):
        self.state = new_state
        self.fitness = 0


# Generates a random state, used for creating the initial population
def generate_state():
    new_state = []
    for i in range(8):
        new_state.append(random.randint(0, 7))
    new_chromosome = Chromosome(new_state)
    new_chromosome.fitness = get_fitness(new_state)
    return new_chromosome


def get_fitness(state) -> int:
    fitness = 28
    for i in range(7):
        j = i + 1
        while j < 8:
            if abs(state[j] - state[i]) == abs(i - j) \
                    or state[j] == state[i]:
                fitness -= 1
            j += 1
    return fitness


def mutate(state) -> int:
    return


def find_pairs(population) -> int:
    return


def solve(population):
    generation_cap = 500
    for i in range(generation_cap):
        find_pairs(population)
    return population


def main():
    init_pop = 10
    population = []
    for i in range(0, init_pop):
        population.append(generate_state())
    solve(population)


if __name__ == "__main__":
    main()
