import individual
import gene


class Population():
    population = []
    gtype = gene.GeneType.NONE
    size = None
    ngen_size = None
    lb = None
    ub = None

    def __init__(self, _size, _ngens, _lb, _ub):
        self.size = _size
        self.lb = _lb
        self.ub = _ub
        self.ngen_size = _ngens

    def init(self):
        for _ in range(0, self.size):
            self.population.append(individual.Individual(self.gtype, self.ngen_size, self.lb, self.ub).init())

    def set_type(self, t):
        self.gtype = t
