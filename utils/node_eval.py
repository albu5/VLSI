# VLSI CAD Project
# Inputs: graph, topo_order, input sequence as input
# inputs sequence should be same as in pi_list and topo_order
# Outputs: output sequence

# We assume primary inputs as first 'npi' nodes in topo_order
# We assume primary outputs as nodes with zero outdegree

# Ashish
# High = 1, Low = 0, Undefined = -1
from logic_eval import logic_eval

def node_eval(graph, inp_list, node, input_sequence):

    logicval = [-1 for i in range(len(graph))]
    count = 0
    for x in inp_list:
        logicval[x] = input_sequence[count]
        count = count+1
    
    outval = rec_eval(graph, logicval, node)
    return outval

def rec_eval(graph, logicval, node):
    children = []
    for i in range(len(graph)):
        if(graph[i][node]>=0):
            children.append(i)
    
    badchild = []
    for child in children:
        if logicval[child]<0:
            badchild.append(child)
            
    if len(badchild)>0:
        for child in badchild:
            logicval[child] = rec_eval(graph, logicval, child)
    
    inlist = []
    for child in children:
        inlist.append(logicval[child])
    
    return logic_eval(inlist, graph[children[0]][node])   

