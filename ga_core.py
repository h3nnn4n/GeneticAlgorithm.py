import population
# import individual
import gene


def main():
    pop = population.Population(10, 10, 0, 1)
    pop.set_type(gene.GeneType.REAL)
    pop.init()
