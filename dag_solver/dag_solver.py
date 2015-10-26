#!/usr/bin/python

# EE677 VLSI Project 
# This function call will evaluate a DAG graph to check its correctness 

# Written by Shashank Gangrade 

_GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}


# graph : adjacency matrix for DAG graph 

# input : List of input nodes
# topo_order : Topological order in subgraph
# output : The output node

# The protocol for graph/nodes is similar to programming assignment

def evaluateDAG(subgraph, input_nodes, topo_order, output_node):
	
	# input in the list 
	# pi is the number of inut nodes in graph which are not neccecarily 5
	pi = len(input_nodes)

	LUT_size = pi					# LUT by definition is 5 input
	LUT_array = (1<<pi);			# Size of final LUT Array (32)
	
	num_sig = len(subgraph)			# Number of signals in graph
	sigval = [-1 for i in range(num_sig)]
	# signal values ( at the output ) of nodes.
    # +1 means HIGH, 0 means LOW, -1 means "undefined"

	LUT = [-4 for i in range(LUT_array)]	# Initilizig LUT list with -1
	input_list  = [[-1 for i in range(LUT_size)]for i in range(LUT_array)]

	# Initializing input_list with all posibble inputs
	for i in range(LUT_array):
		temps = bin(i)[2:].zfill(LUT_size)
		input_list[i] = map(int, temps) 
	
	node_temp = 0

	for i in range(LUT_array):

		for j in range(pi):
			sigval[input_nodes[j]] = input_list[i][j]
				# Part of input_list is applied to all the input nodes
				# This is because number of inputs in current LUT might be less		

		for jj in range(pi,num_sig):			# Computing rest of the nodes other than input
			node_temp = topo_order[jj]			# jj is the first node in topological order
			node_temp_inputs = 0
			temp_input = [-1 for n in range(num_sig)]

			for k in range(jj):
				if subgraph[topo_order[k]][node_temp] > -1 :
					temp_input[node_temp_inputs] = sigval[topo_order[k]]
					node_temp_inputs = node_temp_inputs + 1
#			print(temp_input)		

			# Find the gate corresponding to this node	
			column = []
			for z in range (len(subgraph)):
				row = subgraph[z]
				column.append(row[node_temp])

			gate = max(column)
#			print(gate)

			sigval[node_temp] = nodeSolver(gate, node_temp_inputs, temp_input)			

		LUT[i] = sigval[output_node]
	
	return LUT,input_list

# Solve Node
# Input gate, node_temp_inputs, temp_inputs			
# Output Value of sigval
def nodeSolver( gate, node_temp_inputs, temp_input ) :

	# NAND Operation
	if gate==3 :
		sigval=1
		for m in range(node_temp_inputs):
			sigval = sigval*temp_input[m]

		if	 sigval == 1 :
			sigval = 0
		elif sigval == 0 :
			sigval = 1

	# NOR Operation
	elif gate==5 :
		sigval=0
		for m in range(node_temp_inputs):
			sigval = sigval + temp_input[m]
		
		if sigval > 1 :
			sigval = 1

		if	 sigval == 1 :
			sigval = 0
		elif sigval == 0 :
			sigval = 1


	# OR Operation
	elif gate==4 :
		sigval=0
		for m in range(node_temp_inputs):
			sigval = sigval + temp_input[m]
		if sigval > 1 :
			sigval = 1

	# AND Operation	
	elif gate==2 :
		sigval=1
		for m in range(node_temp_inputs):
			sigval = sigval*temp_input[m]

	# XOR Operation	
	elif gate==6 :
		sigval = temp_input[0]
		for m in range(1,node_temp_inputs):
			sigval = sigval^temp_input[m]

	return sigval


# function call to generate a Adjacency Matrix of DAG for a given combinational circuit

def generateDecoder(n, _GATE):
	nMatrix = n+n+(1<<n)
	mat  = [[-1 for i in range(nMatrix)]for i in range(nMatrix)]
	# mat is the adjacency matrix which contains the decription for DAG defining a decoder

	# Defining first layer connections of NOT gates of each input
	# NOR with one input is NOT
	for z in range(n):
		mat[z][z+n] = _GATE['nor']	

	# Defining secong layer of a set of AND gates
	# The inputs of AND gate will be according to boolean representation of its index in Decoder Outputs
	# xth Decoder output will be AND gate with 0 meaning connection from input or 1 meaning connection from input bar

	pi = [];
	topo = [];

	for i in range(n):
		pi.append(i)

	for i in range(nMatrix):
		topo.append(i)


	for x in range(1<<n):
		temps = bin(x)[2:].zfill(n)
		tempi = map(int, temps) 

		for y in range(n):
			if tempi[y] == 0 :
				mat[n+y][2*n+x] = _GATE['and']

			elif tempi[y] == 1 :
				mat[y][2*n+x] = _GATE['and']

	return mat,topo,pi

## Main Function starts from here, modify to view changes 

n=2
grmat,topo,pi = generateDecoder(n, _GATE)

output_node = 4
LUT, input_list = evaluateDAG(grmat, pi, topo, output_node)

for i in range(4):
	print (input_list[i])
	print (LUT[i])

