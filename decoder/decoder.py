#!/usr/bin/python

#def function = decoder(kwargs):
#	return graph

# EE677 VLSI Project 
# Graph for implementation of generic Decoder
# Written by Shashank Gangrade 
# The logic cicuit of Encoder is one layer of NOT Gates for each inputs, followed by a layer of 

#import math

n = 2;
# Specify the size of decoder
# n bits input 2^n bits output

_GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}


nMatrix = n+n+(1<<n)

mat  = [[-1 for i in range(nMatrix)]for i in range(nMatrix)]

for z in range(n):
	mat[z][z+n] = 3	# nor with one input is not

for x in range(1<<n):
	temps = bin(x)[2:].zfill(n)
	tempi = map(int, temps) 

	for y in range(n):
		if tempi[y] == 0 :
			mat[n+y][2*n+x] = _GATE['and']

		elif tempi[y] == 1 :
			mat[y][2*n+x] = _GATE['and']

for z in range(nMatrix):
	print(mat[z])







