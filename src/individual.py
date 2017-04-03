import gene
import random


class Individual():
    genetic_code = None
    ngenes = None
    lb = None
    ub = None
    gtype = gene.GeneType.NONE
    fitness = 0
    invalid_fitness = True
    mchance = None

    def __init__(self, _gtype,  _ngenes, _lb, _ub):
        self.gtype = _gtype
        self.ngenes = _ngenes
        self.lb = _lb
        self.ub = _ub
        self.genetic_code = []
        self.invalid_fitness = True

    def set_mutation_chance(self, c):
        self.mchance = c

    def init(self):
        self.invalid_fitness = True
        for _ in range(0, self.ngenes):
            self.genetic_code.append(gene.Gene(self.gtype, self.lb, self.ub))

    def add_gene(self, newg):
        self.invalid_fitness = True
        self.genetic_code.append(newg)

    def print(self):
        for i in self.genetic_code:
            print(i.value)

    def mutate(self):
        for g in self.genetic_code:
            if random.uniform(0, 1) < self.mchance:
                g.invalid_fitness = True
                g.mutate()

    def set_fitness(self):
        self.invalid_fitness = False
        self.fitness = 0
        for i in range(1, len(self.genetic_code)):
            if self.genetic_code[i].value % 2 != self.genetic_code[i-1].value % 2:
                self.fitness += 1

    def get_fitness(self):
        if self.invalid_fitness == False:
            return self.fitness
        else:
            return float('NaN')

    def __cmp__(self, other):
        return cmp(self.fitness, other.fitness)

    def __lt(self, other):
        return self.fitness < other.fitness
