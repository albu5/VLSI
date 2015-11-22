# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:04:23 2015

@author: Ashish
"""

from adder.adder import generateAdder
from techMap.genCutset import genCutset
from techMap.trimCutset import trimCutset


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

for rows in graph:
    mystring = ''
    for nodes in rows:
        if(nodes == -1):
            mystring = mystring + '.' + ' '
        else:
            mystring = mystring + str(nodes) + ' '
    print(mystring)
   
mycutset = genCutset(graph, topo_order, pi_list)
for node in range(len(graph)):
    print 'final cutset', node
    print mycutset[node]
    
newcutsets = trimCutset(graph, topo_order, pi_list, mycutset, )
for node in range(len(graph)):
    print 'final cutset', node
    print newcutsets[node]
