import gene


class Individual():
    genetic_code = []
    ngenes = None
    lb = None
    ub = None
    gtype = gene.GeneType.NONE

    def __init__(self, _gtype,  _ngenes, _lb, _ub):
        self.gtype = _gtype
        self.ngenes = _ngenes
        self.lb = _lb
        self.ub = _ub

    def init(self):
        for _ in range(0, self.ngenes):
            self.genetic_code.append(gene.Gene(self.gtype, self.lb, self.ub))

    def add_gene(self, newg):
        self.genetic_code.append(newg)

    def print(self):
        for i in self.genetic_code:
            print(i.value)
