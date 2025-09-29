# walide/fitness.py
from numba import njit

_jitted_fitness = None

def set_fitness_function(func):
    global _jitted_fitness
    _jitted_fitness = njit(func)

@njit
def call_fitness(x):
    global _jitted_fitness
    return _jitted_fitness(x)