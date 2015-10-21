#!/usr/bin/python

# EE677 VLSI Project 
# Graph for implementation of generic Decoder
# Written by Shashank Gangrade 
# The logic cicuit of Encoder is one layer of NOT Gates for each inputs, followed by a layer of AND gates

# n is the size of decoder
# n bits input 2^n bits output

_GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}

def generateDecoder(n, _GATE):

	nMatrix = n+n+(1<<n)

	mat  = [[0 for i in range(nMatrix)]for i in range(nMatrix)]
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

n=3
grmat,topo,pi = generateDecoder(n, _GATE)

nMatrix = n+n+(1<<n)

for z in range(nMatrix):
	print(grmat[z])

print topo
print pi




