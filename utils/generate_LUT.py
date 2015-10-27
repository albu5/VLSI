# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 01:26:51 2015

@author: Ashish
"""

# This routine will form a LUT out of a graph
# Inputs: graph, pi_list, out_node?, topo_order
# Ideally there should be only one out_node in graph
# Outputs: truth_table

from utils.dag_eval import dag_eval
from utils.decbin import dec2bin, bin2dec

def generate_LUT(graph, pi_list, topo_order):
    npi = len(pi_list)
    inputs = range(1<<npi)
    lut = []
    for inp in inputs:
        temp, temp2 = dag_eval(graph, topo_order, dec2bin(inp, npi))
        lut.append(temp)
    return lut
    
