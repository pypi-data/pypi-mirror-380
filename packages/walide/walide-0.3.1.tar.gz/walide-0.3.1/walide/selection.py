# walide/selection.py
import numpy as np
from numba import njit
from .fitness import call_fitness
from .generator import generate_population 

class Selection:
    def __init__(self, pop_size, dimensions, lower_bound, upper_bound, 
                 diversity_threshold=0.05, reset_ratio=0.3, dtype=np.float64):
        self.pop_size = pop_size
        self.dimensions = dimensions
        self.lower_bound = np.array(lower_bound, dtype=dtype)
        self.upper_bound = np.array(upper_bound, dtype=dtype)
        self.diversity_threshold = diversity_threshold
        self.reset_ratio = reset_ratio
        self.dtype = dtype

    def select(self, population, trial):
        parent_fitness = compute_fitness(population, self.pop_size)
        trial_fitness = compute_fitness(trial, self.pop_size)
        
        new_population = select_population(
            population, 
            trial, 
            parent_fitness,
            trial_fitness,
            self.pop_size
        )
        
        diversity = self.calculate_diversity(new_population)
        
        if diversity < self.diversity_threshold:
            new_population = self.reset_partial_population(new_population, parent_fitness, trial_fitness)
            
        return new_population
    
    def calculate_diversity(self, population):
        diversity = 0.0
        for j in range(self.dimensions):
            std = np.std(population[:, j])
            range_val = self.upper_bound[j] - self.lower_bound[j]
            if range_val > 0:
                diversity += std / range_val 
        return diversity / self.dimensions 
    
    def reset_partial_population(self, population, parent_fitness, trial_fitness):
        combined_fitness = np.minimum(parent_fitness, trial_fitness)
        sorted_indices = np.argsort(combined_fitness)
        
        reset_count = max(1, int(self.pop_size * self.reset_ratio))
        reset_indices = sorted_indices[-reset_count:]
        
        new_individuals = generate_population(
            reset_count, 
            self.dimensions, 
            self.lower_bound, 
            self.upper_bound,
            self.dtype
        )
        
        population[reset_indices] = new_individuals
        return population

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