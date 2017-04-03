import individual
import gene
import random


class Population():
    population = None
    gtype = gene.GeneType.NONE
    size = None
    ngen_size = None
    lb = None
    ub = None
    elitism = 0
    elite = None

    mutation_chance = 0.05
    crossover_chance = 0.8

    def __init__(self, _size, _ngens, _lb, _ub):
        self.size = _size
        self.lb = _lb
        self.ub = _ub
        self.ngen_size = _ngens
        self.population = []

    def init(self):
        for _ in range(0, self.size):
            x = None
            x = individual.Individual(self.gtype, self.ngen_size, self.lb, self.ub)
            x.init()
            x.set_mutation_chance(self.mutation_chance)

            self.population.append(x)

    def set_crossover_chance(self, c):
        self.crossover_chance = c
        for x in self.population:
            x.set_mutation_chance(self.mutation_chance)

    def set_mutation_chance(self, c):
        self.mutation_chance = c

    def set_elitism(self, c):
        self.elitism = c
        if self.elitism > 0:
            self.elite = []
        else:
            self.elite = None

    def set_type(self, t):
        self.gtype = t

    def print(self):
        for pop in self.population:
            #print(pop)
            for g in pop.genetic_code:
                print(g.value, end=' ')

            print(" = " + str(pop.fitness))
        print()

    def evo_loop(self, niters):
        for _ in range(0, niters):
            self.print_best()
            self.kelitism_load()
            self.selection()

            self.crossover()
            self.mutation()

            self.kelitism_load()

            self.evaluate()

    def selection(self):
        self.tourney(2)

    def tourney(self, k):
        pass

    def roulette(self, k):
        pass

    def evaluate(self):
        for ind in self.population:
            ind.set_fitness()

    def print_best(self):
        best = sorted(self.population)[:1].print()

    def kelitism_load(self):
        if self.elitism > 0:
            self.elite = sorted(self.population)[:self.elitism]

    def kelitism_save(self):
        if self.elitism > 0:
            for k, v in enumeate(self.elitism):
                self.population[k] = v

    def mutation(self):
        for ind in self.population:
            ind.mutate()

    def crossover(self):
        if random.uniform(0, 1) < self.crossover_chance:
            p1 = random.randint(0, len(self.population) - 1)
            p2 = random.randint(0, len(self.population) - 1)

            while p1 == p2:
                p1 = random.randint(0, len(self.population) - 1)
                p2 = random.randint(0, len(self.population) - 1)

            self.crossover_uniform(p1, p2)

    def crossover_slice(self, p1, p2):
        pass

    def crossover_uniform(self, p1, p2):
        for i in range(0, len(self.population[p1].genetic_code)):
            if random.random() < 0.5:
                a = self.population[p1].genetic_code[i]
                self.population[p1].genetic_code[i] = self.population[p2].genetic_code[i]
                self.population[p2].genetic_code[i] = a
                self.population[p1].set_fitness()
                self.population[p2].set_fitness()
