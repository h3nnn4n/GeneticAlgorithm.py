from enum import Enum
import sys
import random
import math


class GeneType(Enum):
    NONE = 0
    BOOL = 1
    INT = 2
    REAL = 3
    PERMUT = 4


class Gene():
    gene_type = GeneType.NONE

    value = None

    lb = None
    ub = None

    def __init__(self, _gt, _lb, _ub):
        self.gene_type = _gt
        self.lb = _lb
        self.ub = _ub
        self.random_init()

    def random_init(self):
        if self.gene_type == GeneType.NONE:
            raise NotImplementedError

        elif self.gene_type == GeneType.BOOL:
            self.value = random.randint(0, 1) == 1

        elif self.gene_type == GeneType.INT:
            self.value = random.randint(self.lb, self.ub)

        elif self.gene_type == GeneType.REAL:
            self.value = random.uniform(self.lb, self.ub)

        elif self.gene_type == GeneType.PERMUT:
            raise NotImplementedError

    def mutate(self):
        if self.gene_type == GeneType.NONE:
            raise NotImplementedError

        elif self.gene_type == GeneType.BOOL:
            self.value = not self.value

        elif self.gene_type == GeneType.INT:
            old = self.value
            dist = int(math.ceil((self.ub - self.lb) * 0.2))
            self.value += random.randint(-dist, dist)
            if self.value > self.ub or self.value < self.lb:
                self.value = old

        elif self.gene_type == GeneType.REAL:
            old = self.value
            dist = math.ceil((self.ub - self.lb) * 0.05)
            self.value += random.uniform(self.value, dist)
            if self.value > self.ub or self.value < self.lb:
                self.value = old

        elif self.gene_type == GeneType.PERMUT:
            raise NotImplementedError
