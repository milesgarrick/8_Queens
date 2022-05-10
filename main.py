import numpy as np


def generate_state():
    return


def get_fitness(state) -> int:
    return


def mutate(state) -> int:
    return


def solve(population):
    return


def main():
    init_pop = 10
    population = np.array()
    for i in range(0, init_pop-1):
        np.append(population, generate_state())
    solve(population)


if __name__ == "__main__":
    main()