#1. M[i][j] = -1 invalid (no) edge
#2. M[i][j] = 0 constant 0 at node j
#3. M[i][j] = 1 constant 1 at node j
#4. M[i][j] = 2 and gate at node j
#5. M[i][j] = 3 nand gate at node j
#6. M[i][j] = 4 or gate at node j
#7. M[i][j] = 5 nor gate at node j
#8. M[i][j] = 6 xor gate at node j
#9. M[i][j] = 7 xnor gate at node j

'''
This function generates a n-bit ripple carry adder DAG
function inputs: n (no. of bits in one of the input numbers)
funtion outputs:    graph (adjacency matrix with convention described in README.md)
                    topo_order (list of nodes of graph in topological order)
                    pi_list (list of primary input nodes)
'''
def generateAdder(size):
    _GATE = {'0':0,
         '1':1,
         'and':2,
         'nand':3,
         'or':4,
         'nor':5,
         'xor':6,
         'xnor':7}
    # init grmat which contains the graph, topo order and pi_list
    grmat = [[-1 for x in range(7*size)] for x in range(7*size)] 
    topo_order = [];
    pi_list = [];

    # single loop of "size" interations as there is just one fat layer
    # thus expect grmat to be concentrated around diagonal

    for i in range(size):
        topo_order.append(7*i+0)    # A[i]
        topo_order.append(7*i+1)    # B[i]

        pi_list.append(7*i+0)
        pi_list.append(7*i+1)

    for i in range(size):
        # since first carry is zero first element will be different
        if (i > 0):

            # Just for more informative code
            A = 7*i+0
            B = 7*i+1
            X = 7*i+2
            AU = 7*i+3
            AD = 7*i+4
            S = 7*i+5
            C = 7*i+6

            # First XOR gate (X[i] = A[i] xor B[i])
            grmat[A][X] = _GATE['xor']
            grmat[B][X] = _GATE['xor']
            topo_order.append(X)    # X[i]


            # Lower AND gate (AD[i] = A[i] and B[i])
            grmat[A][AD] = _GATE['and']
            grmat[B][AD] = _GATE['and']
            topo_order.append(AD)    # AD[i]


            # Second XOR gate (S[i] = X[i] xor C[i-1])
            grmat[X][S] = _GATE['xor']
            grmat[7*(i-1)+6][S] = _GATE['xor']
            topo_order.append(S)    # S[i]


            # Upper AND gate (AU[i] = X[i] and C[i-1])
            grmat[X][AU] = _GATE['and']
            grmat[7*(i-1)+6][AU] = _GATE['and']
            topo_order.append(AU)    # AU[i]


            # OR gate (C[i] = AU[i] and AD[i])
            grmat[AU][C] = _GATE['or']
            grmat[AD][C] = _GATE['or']
            topo_order.append(C)    # C[i]

        else:
            A = 7*i+0
            B = 7*i+1
            X = 7*i+2
            AU = 7*i+3
            AD = 7*i+4
            S = 7*i+5
            C = 7*i+6
            # First layer has zero carry, hence sligh changes in gates
            # First XOR gate (X[i] = A[i] xor B[i])
            
            grmat[A][X] = _GATE['xor']
            grmat[B][X] = _GATE['xor']
            topo_order.append(X)    # X[i]


            # Lower AND gate (AD[i] = A[i] and B[i])
            grmat[A][AD] = _GATE['and']
            grmat[B][AD] = _GATE['and']
            topo_order.append(AD)    # AD[i]


            # Second XOR gate (S[i] = X[i] xor C[i-1])
            grmat[X][S] = _GATE['or']
            topo_order.append(S)    # S[i]


            # Upper AND gate (AU[i] = X[i] and C[i-1])
            grmat[X][AU] = _GATE['0']
            topo_order.append(AU)    # AU[i]


            # OR gate (C[i] = AU[i] and AD[i])
            grmat[AU][C] = _GATE['or']
            grmat[AD][C] = _GATE['or']
            topo_order.append(C)    # C[i]


    return grmat, topo_order, pi_list

# Uncomment to view a adder DAG
'''
grmat, topo, pi = generateAddder(4)


for rows in grmat:
    mystring = ''
    for nodes in rows:
        if(nodes == -1):
            mystring = mystring + '.' + ' '
        else:
            mystring = mystring + str(nodes) + ' '
    print(mystring)
'''
