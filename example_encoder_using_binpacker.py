# Author: Sagun Pai (Famguy)
from pprint import pprint
from copy import deepcopy

from encoder.encoder_circuit import generateEncoder

# given input dag_graph, we shall use the bin backing approach to get LUTs of specific size

# dag for 8 bit encoder

dag_graph1,pi,po = generateEncoder(8)

from bin_packer.bpmodule import *
from utils.blif import *

printgraph(dag_graph1)
print "------------------------------"
dg,tp = decompose(dag_graph1, 3)

print "------------------------------"

dgt = zip(*dg)

printgraph(dgt)

graph2blif(dgt,tp,pi,po,"8bit_encoder_LUTsize_3.blif")
