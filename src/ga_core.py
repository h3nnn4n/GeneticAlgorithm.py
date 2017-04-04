import population
# import individual
import gene


def main():
    pop = population.Population(50, 100, 0, 10)
    pop.set_type(gene.GeneType.INT)
    pop.init()
    pop.set_mutation_chance(0.05)
    pop.set_crossover_chance(0.8)
    pop.set_elitism(2)

    #pop.print()

    pop.evo_loop(10000)

    #pop.print()
