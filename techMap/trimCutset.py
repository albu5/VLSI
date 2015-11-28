# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:04:23 2015

@author: Ashish
"""

'''
This function trims a list of cuts to form a list of K-feasible cuts for a graph
A K-feasible cut is a set of nodes (set A) such that a set of nodes (set B)
where each node in B is input to some node of A has size (size of B) atmost K

outputs: newCutsets (list of K-feasible cuts of each node)
'''

from sets import Set
def trimCutset(graph, topo_order, pi_list, cutsets, K):
    newCutsets = []
    for nodes in cutsets:
        newCutsets.append([])
        for cutset in nodes:
            inpnodes = []
            for somenode in cutset:
                if somenode in pi_list:
                    if somenode not in inpnodes:
                        inpnodes.append(somenode)
                else:
                    for i in range(len(graph)):
                        if (i not in cutset) & (graph[i][somenode]>=0) & (i not in inpnodes):
                            inpnodes.append(i)
            print inpnodes
            if len(inpnodes)<=K:
                newCutsets[-1].append(cutset)
    return newCutsets

'''
# test case
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
 
newcutsets = trimCutset(graph, mycutset, 2)

for node in range(len(graph)):
    print 'final cutset', node
    print newcutsets[node]
'''
