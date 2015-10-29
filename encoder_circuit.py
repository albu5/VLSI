# Author: Sagun Pai (Famguy)
# Codename: We're beautiful now
# Timestamp: 3rd Oct 2015, 12:29 AM
# Location: Room no 286, Hostel 2, IIT Bombay, Powai

import math

# n-bit encoder assumed, logn outputs
n = 16
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

print encoder_circuit

# encoder_circuit stores various outputs in terms of input signals that need to be fed into an or gate.
# k outputs, each with n/2 inputs connected to an OR gate


