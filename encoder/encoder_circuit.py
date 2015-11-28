# Author: Sagun Pai (Famguy)
# Codename: We're beautiful now
# Timestamp: 3rd Oct 2015, 12:29 AM
# Location: Room no 286, Hostel 2, IIT Bombay, Powai

import math

# n-bit encoder assumed, logn outputs

def generateEncoder(n):
	n = 8
	k = int(math.log(n,2))
	output = [[0]*k]*n
	encoder_circuit = [[] for x in range(k)]

	for index in range(n):
		z = str("{0:b}".format(index))
		while len (z) < k:
			z = "0" + z
		output[index] = list(z)

	#print output

	for entry_index, entry in enumerate(output):
		for i,j in enumerate(entry):
			if j == '1':
				if entry_index not in encoder_circuit[i]:
					encoder_circuit[i].append(entry_index)

	# print encoder_circuit

	# encoder_circuit stores various outputs in terms of input signals that need to be fed into an or gate.
	# k outputs, each with n/2 inputs connected to an OR gate

	from pprint import pprint

	nodes = n+k
	dag_graph = [[-1 for s in range(nodes)] for s in range(nodes)]
	# 0 to n-1 we have inputs
	# n to n+k-1 we have outputs (or gates)


	for i,e in enumerate(reversed(encoder_circuit)):
		for j in e:
			dag_graph[i+n][j] = 4
		#	dag_graph[j][i+n] = 4


	print dag_graph

	pilist = range(0,n)
	polist = range(n,n+k)

	print pilist
	print polist
	return dag_graph,pilist,polist
