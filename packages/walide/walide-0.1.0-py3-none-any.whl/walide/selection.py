# walide/selection.py
import numpy as np
from numba import njit
from .fitness import call_fitness

class Selection:
    def __init__(self, pop_size, dimensions, dtype=np.float64):
        self.pop_size = pop_size
        self.dimensions = dimensions
        self.dtype = dtype

    def select(self, population, trial):
        parent_fitness = compute_fitness(population, self.pop_size)
        trial_fitness = compute_fitness(trial, self.pop_size)
        
        return select_population(
            population, 
            trial, 
            parent_fitness,
            trial_fitness,
            self.pop_size
        )

@njit
def compute_fitness(population, pop_size):
    fitness = np.empty(pop_size, dtype=np.float64)
    for i in range(pop_size):
        fitness[i] = call_fitness(population[i])
    return fitness

@njit
def select_population(population, trial, parent_fitness, trial_fitness, pop_size):
    new_population = np.empty_like(population)
    for i in range(pop_size):
        if trial_fitness[i] <= parent_fitness[i]:
            new_population[i] = trial[i]
        else:
            new_population[i] = population[i]
    return new_population