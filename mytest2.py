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
from utils.generate_LUT import generate_LUT 

    

    

nodes = 6
sub  = [[-1 for i in range(nodes)]for i in range(nodes)]
sub[0][5] = 6
sub[1][5] = 6
sub[2][5] = 6
sub[3][5] = 6
sub[4][5] = 6

pi_list = [0, 1, 2, 3, 4]
topo_order = [0, 1, 2, 3, 4, 5]

lut = generate_LUT(sub, pi_list, topo_order)
inputs = range(1<<len(pi_list))

for i in inputs:
    print dec2bin(i, len(pi_list))
    print lut[i]
    