# walide/generator.py
import numpy as np
from numba import njit

class Generator:
    def __init__(self, dimension, pop_size, lower_bound, upper_bound, dtype=np.float64):
        self.pop_size = pop_size
        self.dimensions = dimension
        self.lower_bound = np.array(lower_bound, dtype=dtype)
        self.upper_bound = np.array(upper_bound, dtype=dtype)
        self.dtype = dtype
    
    def generate(self):
        return generate_population(
            self.pop_size, 
            self.dimensions, 
            self.lower_bound, 
            self.upper_bound,
            self.dtype
        )

@njit
def generate_population(pop_size, dimensions, lower_bound, upper_bound, dtype):
    population = np.empty((pop_size, dimensions), dtype=dtype)
    for i in range(pop_size):
        for j in range(dimensions):
            population[i, j] = np.random.uniform(low=lower_bound[j], high=upper_bound[j])
    return population