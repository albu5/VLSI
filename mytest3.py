# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 04:37:07 2015

@author: Ashish
"""

from techMap.generateCutset import generateCutset

graph = [[-1 for x in range(8)]for y in range(8)]
topo_order = range(8)
pi_list = range(3)
print graph
graph[0][3] = 1
graph[0][4] = 1
graph[1][3] = 1
graph[1][4] = 1
graph[2][5] = 1
graph[2][6] = 1
graph[3][7] = 1
graph[4][5] = 1
graph[4][6] = 1
graph[5][7] = 1

cutset = generateCutset(graph, topo_order, pi_list)
