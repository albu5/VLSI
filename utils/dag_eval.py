# VLSI CAD Project
# Inputs: graph, topo_order, input sequence as input
# inputs sequence should be same as in pi_list and topo_order
# Outputs: output sequence

# We assume primary inputs as first 'npi' nodes in topo_order
# We assume primary outputs as nodes with zero outdegree

# Ashish
# High = 1, Low = 0, Undefined = -1
from logic_eval import logic_eval

def dag_eval(adjmat, topo_order, input_sequence):

    npi = len(input_sequence)
    nV = len(topo_order)
    
    # Initialize node outputs as invalid
    node_val = [-1 for i in range(nV)]

    # Obtain pi_list
    pi_list = []
    for i in range(npi):
        pi_list.append(topo_order[i])

    # Obtain po_list
    po_list = topo_order[:]
    for inV in topo_order:
        flag = 0
        for outV in topo_order:
            if adjmat[inV][outV] >= 0:
                flag = 1
        if flag == 1:
            po_list.remove(inV)
    
    for i in pi_list:
        node_val[i] = input_sequence[i]

    
    # Assign values to nodes
    for node in topo_order:
        # Assign values to input nodes
        if node in pi_list:
            node_val[node] = input_sequence[node]
            
        # Assign values to rest of the nodes
        else:
            # 'inlist' contains all input nodes to the gate 'gate'
            inlist = []
            # -1 is an invalid gate
            gate = -1
            for inp in topo_order:
                if adjmat[inp][node] >= 0:
                    inlist.append(node_val[inp])
                    gate = adjmat[inp][node]
                    
            node_val[node] = logic_eval(inlist, gate)

    # Get output sequence now
    output_sequence = []
    for node in po_list:
        output_sequence.append(node_val[node])
    
    return output_sequence, node_val
