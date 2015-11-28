# Updated Tasks
Add comments to whatever file you contributed to.

Everyone for each DAG Adjacency Matrix, also output topologial order and primary input nodes.
# VLSI
Created Git
Create methods in python to generate graph (Adjacency Matrix) for:
1. Decoder - Shashank
2. Encoder - Sagun
3. Adder - Ashish

Adjacecny Matrix [M] conventions:
for edge from node i to j:

#Reccomended: Use this as dictionary, will be helpful later
Just use M[i][j] = _GATE['or'] instead of M[i][j] = 6

1. M[i][j] = -1 invalid (no) edge
2. M[i][j] = 0 constant 0 at node j
3. M[i][j] = 1 constant 1 at node j
4. M[i][j] = 2 and gate at node j
5. M[i][j] = 3 nand gate at node j
6. M[i][j] = 4 or gate at node j
7. M[i][j] = 5 nor gate at node j
8. M[i][j] = 6 xor gate at node j
9. M[i][j] = 7 xnor gate at node j

# Dictionary
_GATE = {'0':0,
         '1':1,
         'and':2,
         'nand':3,
         'or':4,
         'nor':5,
         'xor':6,
         'xnor':7}

NOTE:
1. buffer is same as or/and/xor gate with one input
2. inverter is same as nor/nand/xnor gate with one input

Suggestion - Please put all your files you made in some folder named after the topic you've picked up and send the pull request. Also, keep the source code as modular (function definitions instead of plain source code).

# Examples
example_LUT.py contains exaple of LUT fitting and writing blif file
