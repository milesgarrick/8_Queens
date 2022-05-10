import random
import math
import copy


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


def get_total_fitness(population) -> int:
    new_total_fitness = 0
    for i in population:
        new_total_fitness += i.fitness
    return new_total_fitness


# Determines if a child will mutate, then randomly selects a column
# to randomize.
def mutate(child):
    p = random.randint(0, 100)
    if p <= 5:
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        child.state[i] = j


# Randomly selects a locus for crossover and generates new children.
# Passes children into mutate function then appends to new_pop.
def propagate(parents, new_pop, total_fitness):
    locus = random.randint(1, 7)
    new_state = []
    for i in range(0, locus):
        new_state.append(parents[0].state[i])
    for i in range(locus, 8):
        new_state.append(parents[1].state[i])
    child1 = Chromosome(new_state)
    child1.fitness = get_fitness(child1.state)
    new_state = []
    for i in range(0, locus):
        new_state.append(parents[1].state[i])
    for i in range(locus, 8):
        new_state.append(parents[0].state[i])
    child2 = Chromosome(new_state)
    child2.fitness = get_fitness(child2.state)
    del new_state
    mutate(child1)
    mutate(child2)
    new_pop.append(child1)
    new_pop.append(child2)
    return


def find_pairs(population, total_fitness, new_pop):
    parents = []
    while len(parents) < 2:
        i = random.randint(0, len(population)-1)
        p = population[i].fitness / total_fitness
        rand = random.random()
        if rand <= p:
            parents.append(population[i])
    propagate(parents, new_pop, total_fitness)


def solve(population, total_fitness, init_pop):
    generation_cap = 500
    for i in range(generation_cap):
        new_pop = []
        for j in range(math.floor(init_pop / 2)):
            find_pairs(population, total_fitness, new_pop)
        total_fitness = get_total_fitness(new_pop)
        del population
        population = new_pop
        del new_pop
    return population, total_fitness


def main():
    init_pop = 50
    population = []
    total_fitness = 0
    for i in range(0, init_pop):
        population.append(generate_state())
        total_fitness += population[i].fitness
    print("Starting generation:\n")
    for i in population:
        print(i.state)
    starting_avg = total_fitness / init_pop
    population, total_fitness = solve(population, total_fitness, init_pop)
    print("Final generation:\n")
    for i in population:
        print(i.state)
    print("Starting average fitness: ", starting_avg)
    print("Average fitness: ", total_fitness / init_pop)


if __name__ == "__main__":
    main()
