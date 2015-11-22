# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:37:27 2015

@author: Ashish
"""

from adder.adder import generateAdder
from techMap.genCutset import genCutset
from techMap.trimCutset import trimCutset

#create graph
graph = [[-1 for x in range(8)]for y in range(8)]
topo_order = range(8)
pi_list = range(3)
graph[0][3] = 1
graph[0][4] = 1
graph[1][3] = 1
graph[1][4] = 1
graph[2][5] = 1
graph[2][6] = 1
graph[3][7] = 1
graph[4][5] = 1
graph[4][6] = 1
graph[5][7] = 1

#display graph
for rows in graph:
    mystring = ''
    for nodes in rows:
        if(nodes == -1):
            mystring = mystring + '.' + ' '
        else:
            mystring = mystring + str(nodes) + ' '
    print(mystring)
   
#obtain cutsets
cutset = genCutset(graph, topo_order, pi_list)
for node in range(len(graph)):
    print 'final cutset', node
    print cutset[node]

#obtain k-feasible cutsets
ncutsets = trimCutset(graph, topo_order, pi_list, cutset, 3)
for node in range(len(graph)):
    print 'final cutset', node
    print ncutsets[node]

#initialize lut mapped graph
ngraph = [[-1 for x in range(len(graph))]for y in range(len(graph))]
npi_list = []
ntopo_order = []

#obtain primary outputs
po_list = []
for i in range(len(graph)):
    node = topo_order[-(i+1)]
    po_list.append(node)
    for j in range(len(graph)):
        if graph[node][j]>=0:
            po_list.remove(node)
            break

print po_list

K = 3

def fitnodes(graph, topo_order, pi_list, po_list, ncutsets, ngraph, ntopo_order, npi_list, K):
    print po_list
    new_po_list = []
    for node in po_list:
        new_po_list = []
        ntopo_order.append(node)
        if node not in pi_list:
            #??????????????????????????????????????
            cutset = ncutsets[nodes][0]
            #??????????????????????????????????????
            inpnodes = []
            for somenode in cutset:
                if somenode in pi_list:
                    if somenode not in inpnodes:
                        inpnodes.append(somenode)
                else:
                    for i in range(len(graph)):
                        if (i not in cutset) & (graph[i][somenode]>=0) & (i not in inpnodes):
                            inpnodes.append(i)
            temp = new_po_list + inpnodes
            new_po_list = list(set(temp))
            for x in inpnodes:
                print x
                print node
                ngraph[x][node] = 1
                #replace this by lut number
        else:
            npi_list.append(node)
    if len(new_po_list)>0:
        fitnodes(graph, topo_order, pi_list, new_po_list, ncutsets, ngraph, ntopo_order, npi_list, K)
    

fitnodes(graph, topo_order, pi_list, po_list, ncutsets, ngraph, ntopo_order, npi_list, K)
ntopo_order.reverse()

#display graph
for rows in ngraph:
    mystring = ''
    for nodes in rows:
        if(nodes == -1):
            mystring = mystring + '.' + ' '
        else:
            mystring = mystring + str(nodes) + ' '
    print(mystring)