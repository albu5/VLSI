# Author: Sagun Pai (Famguy)
from pprint import pprint
from copy import deepcopy

# given input dag_graph, we shall use the bin backing approach to get LUTs of specific size

# dag for 8 bit encoder

dag_graph1 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 4, -1, 4, -1, 4, -1, 4, -1, -1, -1], [-1, -1, 4, 4, -1, -1, 4, 4, -1, -1, -1], [-1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1]]

pi = [0, 1, 2, 3, 4, 5, 6, 7]
po = [8, 9, 10]


from bin_packer.bpmodule import *
from utils.blif import *

printgraph(dag_graph1)
print "------------------------------"
dg,tp = decompose(dag_graph1, 3)

print "------------------------------"

dgt = zip(*dg)

printgraph(dgt)

graph2blif(dgt,tp,pi,po,"8bit_encoder_LUTsize_3.blif")
