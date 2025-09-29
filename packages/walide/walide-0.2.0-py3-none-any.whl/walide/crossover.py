# walide/crossover.py
import numpy as np
from numba import njit

class Crossover:
    def __init__(self, pop_size, dimensions, lower_bound, upper_bound, cr, dtype=np.float64):
        self.pop_size = pop_size
        self.dimensions = dimensions
        self.lower_bound = np.array(lower_bound, dtype=dtype)
        self.upper_bound = np.array(upper_bound, dtype=dtype)
        self.cr = cr
        self.dtype = dtype

    def crossover(self, population, mutant):
        trial = crossover_population(
            population, 
            mutant, 
            self.pop_size, 
            self.dimensions, 
            self.cr,
            self.lower_bound,
            self.upper_bound
        )
        return trial

@njit
def crossover_population(population, mutant, pop_size, dimensions, cr, lower_bound, upper_bound):
    trial = np.empty_like(population)
    
    for i in range(pop_size):

        force_dim = np.random.randint(dimensions)
        for j in range(dimensions):
            if np.random.rand() < cr or j == force_dim:
                trial[i, j] = mutant[i, j]
            else:
                trial[i, j] = population[i, j]
        
        # 边界处理
        for j in range(dimensions):
            if trial[i, j] < lower_bound[j]:
                trial[i, j] = lower_bound[j]
            elif trial[i, j] > upper_bound[j]:
                trial[i, j] = upper_bound[j]
    
    return trial