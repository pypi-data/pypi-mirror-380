# walide/de.py
import numpy as np
from .generator import Generator
from .mutate import Mutate
from .crossover import Crossover
from .selection import Selection, compute_fitness
from .fitness import set_fitness_function

class DE:
    def __init__(self, func, dim, popsize=50, lb=None, ub=None, 
                 f1=0.9, f2=0.1, cr=0.9, maxiter=100, log=False, dtype=np.float64):
        self.func = func
        self.dim = dim
        self.popsize = popsize
        self.maxiter = maxiter
        self.logging = log
        self.pop = None
        self.fitness = None
        self.dtype = dtype
        
        if lb is None:
            self.lower_bound = np.zeros(dim, dtype=dtype)
        else:
            self.lower_bound = np.array(lb, dtype=dtype) if np.size(lb) > 1 else np.full(dim, lb, dtype=dtype)
            
        if ub is None:
            self.upper_bound = np.ones(dim, dtype=dtype)
        else:
            self.upper_bound = np.array(ub, dtype=dtype) if np.size(ub) > 1 else np.full(dim, ub, dtype=dtype)
        
        self.generator = Generator(
            dimension=dim, 
            pop_size=popsize,
            lower_bound=self.lower_bound, 
            upper_bound=self.upper_bound,
            dtype=dtype
        )
        self.mutate = None
        self.crossover = Crossover(
            pop_size=popsize, 
            dimensions=dim,
            lower_bound=self.lower_bound, 
            upper_bound=self.upper_bound, 
            cr=cr,
            dtype=dtype
        )
        self.selection = Selection(
            pop_size=popsize, 
            dimensions=dim,
            dtype=dtype
        )
        
        self.f1 = f1
        self.f2 = f2
        self.cr = cr
        
        self.best_cost = []
        self.best_position = None
        self.best_fitness = np.inf
        set_fitness_function(func)

    def reset(self, **kwargs):
        old_dim = self.dim
        old_popsize = self.popsize
        old_lower = self.lower_bound
        old_upper = self.upper_bound

        if 'dim' in kwargs and kwargs['dim'] != self.dim:
            self.dim = kwargs['dim']
            
            if 'lower_bound' not in kwargs:
                kwargs['lower_bound'] = np.full(self.dim, old_lower[0], dtype=self.dtype)
            if 'upper_bound' not in kwargs:
                kwargs['upper_bound'] = np.full(self.dim, old_upper[0], dtype=self.dtype)
        
        if 'popsize' in kwargs:
            self.popsize = kwargs['popsize']
        
        if 'lower_bound' in kwargs:
            self.lower_bound = np.array(kwargs['lower_bound'], dtype=self.dtype) if np.size(kwargs['lower_bound']) > 1 else np.full(self.dim, kwargs['lower_bound'], dtype=self.dtype)
        if 'upper_bound' in kwargs:
            self.upper_bound = np.array(kwargs['upper_bound'], dtype=self.dtype) if np.size(kwargs['upper_bound']) > 1 else np.full(self.dim, kwargs['upper_bound'], dtype=self.dtype)
        
        for param in ['f1', 'f2', 'cr', 'maxiter', 'dtype']:
            if param in kwargs:
                setattr(self, param, kwargs[param])
        
        self.generator = Generator(
            dimension=self.dim,
            pop_size=self.popsize,
            lower_bound=self.lower_bound,
            upper_bound=self.upper_bound,
            dtype=self.dtype
        )
        
        self.crossover = Crossover(
            pop_size=self.popsize,
            dimensions=self.dim,
            lower_bound=self.lower_bound,
            upper_bound=self.upper_bound,
            cr=self.cr,
            dtype=self.dtype
        )
        
        self.selection = Selection(
            pop_size=self.popsize,
            dimensions=self.dim,
            dtype=self.dtype
        )
        
        if self.best_position is not None:
            if len(self.best_position) != self.dim:
                new_best = np.empty(self.dim, dtype=self.dtype)
                min_len = min(len(self.best_position), self.dim)
                new_best[:min_len] = self.best_position[:min_len]
                new_best[min_len:] = (self.lower_bound[min_len:] + self.upper_bound[min_len:]) / 2
                self.best_position = new_best
        
        self.mutate = Mutate(
            pop_size=self.popsize,
            dimensions=self.dim,
            lower_bound=self.lower_bound,
            upper_bound=self.upper_bound,
            f1=self.f1,
            f2=self.f2,
            best=self.best_position if self.best_position is not None else np.zeros(self.dim, dtype=self.dtype),
            dtype=self.dtype
        )
        
        if self.pop is not None:
            if old_dim != self.dim:
                new_pop = np.empty((self.pop.shape[0], self.dim), dtype=self.dtype)
                min_dim = min(old_dim, self.dim)
                new_pop[:, :min_dim] = self.pop[:, :min_dim]
                new_pop[:, min_dim:] = (self.lower_bound[min_dim:] + self.upper_bound[min_dim:]) / 2
                self.pop = new_pop
            
            if old_popsize != self.popsize:
                if self.popsize > old_popsize:
                    new_individuals = self.generator.generate()[old_popsize:]
                    self.pop = np.vstack((self.pop, new_individuals))
                else:
                    self.pop = self.pop[:self.popsize]
            
            for i in range(self.pop.shape[0]):
                for j in range(self.dim):
                    if self.pop[i, j] < self.lower_bound[j]:
                        self.pop[i, j] = self.lower_bound[j]
                    elif self.pop[i, j] > self.upper_bound[j]:
                        self.pop[i, j] = self.upper_bound[j]
            
            self.fitness = compute_fitness(self.pop, self.popsize)
            
            current_best_idx = np.argmin(self.fitness)
            current_best_fitness = self.fitness[current_best_idx]
            if current_best_fitness < self.best_fitness:
                self.best_fitness = current_best_fitness
                self.best_position = self.pop[current_best_idx].copy()
            if self.best_cost:
                self.best_cost[-1] = self.best_fitness
            else:
                self.best_cost.append(self.best_fitness)
            self.mutate.best = self.best_position

    def optimize(self):
        if self.pop is None:
            population = self.generator.generate()
        else:
            population = self.pop
        
        fitness = compute_fitness(population, self.popsize)
        best_idx = np.argmin(fitness)
        self.best_position = population[best_idx].copy()
        self.best_fitness = fitness[best_idx]
        self.best_cost.append(self.best_fitness)
        
        self.mutate = Mutate(
            pop_size=self.popsize, 
            dimensions=self.dim,
            lower_bound=self.lower_bound, 
            upper_bound=self.upper_bound,
            f1=self.f1, 
            f2=self.f2, 
            best=self.best_position,
            dtype=self.dtype
        )
        
        for gen in range(1, self.maxiter+1):
            mutant = self.mutate.mutate(population)
            trial = self.crossover.crossover(population, mutant)
            population = self.selection.select(population, trial)
            fitness = compute_fitness(population, self.popsize)
            current_best_idx = np.argmin(fitness)
            current_best_fitness = fitness[current_best_idx]
            
            if current_best_fitness < self.best_fitness:
                self.best_fitness = current_best_fitness
                self.best_position = population[current_best_idx].copy()
            
            self.best_cost.append(self.best_fitness)
            self.mutate.best = self.best_position

            sorted_indices = np.argsort(-fitness)
            self.pop = population[sorted_indices]
            self.fitness = fitness[sorted_indices]
            
            if self.logging and (gen % 100 == 0 or gen == self.maxiter):
                print(f"{gen} {self.best_fitness:.12f} {self.f1:.2f} {self.f2:.2f} {self.cr:.2f}")
        
        return self.best_position, self.best_fitness

    def save(self, file_path=None):
        if self.pop is not None:
            default_path = 'population.csv'
            path = default_path if file_path is None else file_path
            np.savetxt(path, self.pop, delimiter=',')
    def load(self, file_path):
        try:
            self.pop = np.loadtxt(file_path, delimiter=',', dtype=self.dtype)
            self.popsize = self.pop.shape[0]
            self.dim = self.pop.shape[1]
            self.fitness = compute_fitness(self.pop, self.popsize)
            current_best_idx = np.argmin(self.fitness)
            current_best_fitness = self.fitness[current_best_idx]
            if current_best_fitness < self.best_fitness:
                self.best_fitness = current_best_fitness
                self.best_position = self.pop[current_best_idx].copy()
            if self.best_cost:
                self.best_cost[-1] = self.best_fitness
            else:
                self.best_cost.append(self.best_fitness)
            self.mutate = Mutate(
                pop_size=self.popsize,
                dimensions=self.dim,
                lower_bound=self.lower_bound,
                upper_bound=self.upper_bound,
                f1=self.f1,
                f2=self.f2,
                best=self.best_position,
                dtype=self.dtype
            )
        except Exception as e:
            print(f"{e}")
