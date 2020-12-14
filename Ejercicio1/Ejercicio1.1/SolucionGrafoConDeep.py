# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:18:21 2020

@author: Juan Guillermo Laura Mamani
"""

import array
import random

import numpy 
import pandas as pd

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

grafo=pd.read_csv('C:/Users/Yuki/Desktop/Nueva carpeta/Ejercicio1/grafo.csv', sep=';',header=None)
print(grafo.values)

distancia_mapa = grafo
IND_SIZE = 4

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalGraf(individual):
    distancia = distancia_mapa[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distancia += distancia_mapa[gene1][gene2]
  
    return distancia,

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalGraf)

def main():
    random.seed(169)

    pop = toolbox.population(n=300)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 40, stats=stats, 
                        halloffame=hof)
    
    return pop, stats, hof

if __name__ == "__main__":
    pop, log, hof = main()
    
    print('Ruta Optima')
    print(hof)
  

    