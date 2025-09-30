# walide/mutate.py
import numpy as np
from numba import njit

class Mutate:
    def __init__(self, pop_size, dimensions, lower_bound, upper_bound, f1, f2, best, dtype=np.float64):
        self.pop_size = pop_size
        self.dimensions = dimensions
        self.lower_bound = np.array(lower_bound, dtype=dtype)
        self.upper_bound = np.array(upper_bound, dtype=dtype)
        self.f1 = f1
        self.f2 = f2
        self.best = np.array(best, dtype=dtype)
        self.dtype = dtype

    def mutate(self, population):
        mutant = mutate_population(
            population, 
            self.pop_size, 
            self.dimensions,
            self.f1, 
            self.f2, 
            self.best,
            self.lower_bound,
            self.upper_bound
        )
        return mutant

@njit
def mutate_population(population, pop_size, dimensions, f1, f2, best, lower_bound, upper_bound):
    mutant = np.empty_like(population)
    for i in range(pop_size):
        indices = np.zeros(3, dtype=np.int32)
        found = 0
        while found < 3:
            idx = np.random.randint(pop_size)
            if idx != i and idx not in indices[:found]:
                indices[found] = idx
                found += 1
        r1, r2, r3 = indices
        
        for j in range(dimensions):
            mutant[i, j] = population[r1, j] + f1 * (population[r2, j] - population[r3, j]) + f2 * (best[j] - population[r1, j])
        
        for j in range(dimensions):
            if mutant[i, j] < lower_bound[j]:
                mutant[i, j] = lower_bound[j]
            elif mutant[i, j] > upper_bound[j]:
                mutant[i, j] = upper_bound[j]
    
    return mutant