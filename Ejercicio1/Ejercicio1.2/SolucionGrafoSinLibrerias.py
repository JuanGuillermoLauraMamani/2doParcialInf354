# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:37:29 2020

@author: juan Guillermo Laura Mamani
"""

import random
import pandas as pd
import math

grafo=pd.read_csv('C:/Users/Yuki/Desktop/Nueva carpeta/Ejercicio1/grafo.csv', sep=';',header=None)
print(grafo.values)

poblacion = grafo
scpadres=[]
nueva_poblacion = []
print('*********************Poblacion********************')
print(poblacion)


def funcionEval() :
    global poblacion 
    valores = []
    puntos=[]
    print('*****valores*****')
    for i in range(4) :
        crvalor=0
        
        for j in range(5,0,-1) :
            crvalor += poblacion[i][j]*(2**(5-j))
        crvalor = crvalor if poblacion[i][0]==1 else crvalor
        print(crvalor)
        valores.append((crvalor**3) +(crvalor**2) + crvalor)
   
    print('*****F(x) = x**3+x**2+ x evaluado *****')   
    print(valores)
    valores, poblacion  = zip(*sorted(zip(valores, poblacion) , reverse = True))
  
def calculate_fitness():
    distance = 0
    for i in range(0,len(poblacion)):
        if i < (len(poblacion) - 1):
            xDistance = abs(poblacion[i][1] - poblacion[i+1][1])
            yDistance = abs(poblacion[i][2] - poblacion[i+1][2])
        else:
            xDistance = abs(poblacion[i][1] - poblacion[0][1])
            yDistance = abs(poblacion[i][2] - poblacion[0][2])
        distance += math.sqrt((xDistance**2)+(yDistance**2))
    print(distance)
    
def seleccion():
    global scpadres
    scpadres=poblacion[0:4]
    
    print('***** mejor individuo*****')
    print(scpadres)
    
    

def cruce() :
    global scpadres
    
    pcruce = random.randint(0,4)
    scpadres =scpadres + tuple([(scpadres[0][0:pcruce +1] +scpadres[1][pcruce+1:4])])
    scpadres =scpadres+ tuple([(scpadres[1][0:pcruce +1] +scpadres[0][pcruce+1:4])])
    
    print(scpadres)
    


def mutacion() :
    global poblacion, scpadres
    muta = random.randint(0,49)
    if muta == 20 :
        x=random.randint(0,3)
        y = random.randint(0,5)
        scpadres[x][y] = 1-scpadres[x][y]
    poblacion  = scpadres
    print(poblacion)

    


for i in range(3) :
    calculate_fitness()
    seleccion() 
    print('***** cruce*****')
    cruce()
    print('***** mutacion*****')
    mutacion()
    
