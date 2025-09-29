# waliswarm/de.py
import numpy as np
from .generator import Generator
from .mutate import Mutate
from .crossover import Crossover
from .selection import Selection, compute_fitness
from .fitness import set_fitness_function

class DE:
    def __init__(self, func, dim, popsize=50, lower_bound=None, upper_bound=None, 
                 f1=1, f2=0.01, cr=0.95, maxiter=100, logging=False, dtype=np.float64):
        self.func = func
        self.dim = dim
        self.popsize = popsize
        self.maxiter = maxiter
        self.logging = logging
        self.dtype = dtype

        if lower_bound is None:
            self.lower_bound = np.zeros(dim, dtype=dtype)
        else:
            self.lower_bound = np.array(lower_bound, dtype=dtype) if np.size(lower_bound) > 1 else np.full(dim, lower_bound, dtype=dtype)
            
        if upper_bound is None:
            self.upper_bound = np.ones(dim, dtype=dtype)
        else:
            self.upper_bound = np.array(upper_bound, dtype=dtype) if np.size(upper_bound) > 1 else np.full(dim, upper_bound, dtype=dtype)
        
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

    def optimize(self):
        population = self.generator.generate()
        
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
            
            if self.logging and (gen % 100 == 0 or gen == self.maxiter):
                print(f"{gen} {self.best_fitness:.12f} {self.f1:.2f} {self.f2:.2f} {self.cr:.2f}")
        
        return self.best_position, self.best_fitness