# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:37:27 2015

@author: Ashish
"""

from adder.adder import generateAdder
from utils.LUTfit import LUTfit
#create graph
'''
graph = [[-1 for x in range(8)]for y in range(8)]
topo_order = range(8)
pi_list = range(3)
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
'''
graph, topo_order, pi_list = generateAdder(2)
ngraph, ntopo_order, npi_list = LUTfit(graph, topo_order, pi_list, 4, "myadder2.blif")
