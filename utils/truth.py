# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 01:26:51 2015

@author: Ashish
"""

# This routine will form a LUT out of a graph
# Inputs: graph, pi_list, out_node?, topo_order
# Ideally there should be only one out_node in graph
# Outputs: truth_table

from utils.decbin import dec2bin, bin2dec
from utils.node_eval import node_eval

def truth(graph, inp_list, node):
    npi = len(inp_list)
    inputs = range(1<<npi)
    truthin = []
    truthout = []
    for inp in inputs:
        truthout.append(node_eval(graph, inp_list, node, dec2bin(inp, npi)))
        truthin.append(dec2bin(inp, npi))
        
    return truthin, truthout

'''
graph = [[-1 for x in range(7)]for y in range(7)]
pi_list = range(4)
topo_order = range(7)
graph[0][4] = 2
graph[1][4] = 2
graph[2][5] = 2
graph[3][5] = 2
graph[4][6] = 2
graph[5][6] = 2

truthin, truthout = truth(graph, [0, 1, 2, 3], 6)
for i in range(len(truthout)):
    print truthin[i], truthout[i]

'''
