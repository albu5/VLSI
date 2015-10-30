from sets import Set
from adder.adder import generateAdder

graph, topo_order, pi_list = generateAdder(2)
for rows in graph:
    mystring = ''
    for nodes in rows:
        if(nodes == -1):
            mystring = mystring + '.' + ' '
        else:
            mystring = mystring + str(nodes) + ' '
    print(mystring)