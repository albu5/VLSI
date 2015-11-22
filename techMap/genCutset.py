# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 04:37:07 2015

@author: Ashish
"""

from sets import Set

def genCutset(graph, topo_order, pi_list):
    # define a cutset for each node
    cutset = [[] for i in range(max(topo_order)+1)]


    for node in topo_order:
        # each cutset initialized with empty set
        cutset[node].append(Set([]))
        
        input_list = []
        # find nodes input to current nodes
        if not(node in pi_list):
            for inpnode in topo_order:
                if graph[inpnode][node]>=0:
                    input_list.append(inpnode)

        
        # now add more possible cutsets from child nodes in input_list
        for child in input_list:
            temp = cutset[node][:]
            cutset[node] = [existing_set.union(child_set) for existing_set in temp for child_set in cutset[child]]
            cutset[node] = [x for x in cutset[node] if x != Set([])]
        
        cutset[node].append(Set([node]))
        cutset[node] = [x for x in cutset[node] if x != Set([])]

        #debug
        #print 'final cutset', node
        #print cutset[node]
    return cutset

'''
# test case
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
'''
