import population
# import individual
import gene


def main():
    pop = population.Population(10, 10, 0, 10)
    pop.set_type(gene.GeneType.INT)
    pop.init()
    pop.set_mutation_chance(0.1)
    pop.set_crossover_chance(0.8)
    pop.set_elitism(2)

    pop.evaluate()

    #for ind in pop.population:
        #ind.set_fitness()

    pop.print()

    pop.evo_loop(100)

    pop.print()
