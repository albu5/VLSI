# VLSI
Created Git
Create methods in python to generate graph (Adjacency Matrix) for:
1. Decoder - Shashank
2. Encoder - Sagun
3. Multiplier - Ashish
4. Shardul (chose some for yourself)

Adjacecny Matrix [M] conventions:
for edge from node i to j:

1. M[i][j] = -1 invalid (no) edge
2. M[i][j] = 0 or gate at node j
3. M[i][j] = 1 nor gate at node j
4. M[i][j] = 2 and gate at node j
5. M[i][j] = 3 nand gate at node j
6. M[i][j] = 4 xor gate at node j
7. M[i][j] = 5 xnor gate at node j

NOTE:
1. buffer is same as or/and/xor gate with one input
2. inverter is same as nor/nand/xnor gate with one input
