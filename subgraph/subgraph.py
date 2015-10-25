#!/usr/bin/python

# EE677 VLSI Project 
# This function call, fills a single LUT 
# with values according to definition of input subgraph

# Written by Shashank Gangrade 

_GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}


# subgraph : adjacency matrix for small subgraphs with 
# at most 5 inputs and 1 output
# input : List of input nodes
# topo_order : Topological order in subgraph
# output : The output node

def generateLUT(subgraph, input, topo_order, output)
	
	pi = len(input)

	LUT_size = 5
	LUT_array = (1<<5);
	
	# Initilizig LUT list with 

	LUT = [-1 for i in range(LUT_array)]


	




	return LUT