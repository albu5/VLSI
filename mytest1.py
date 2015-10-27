










'''
from adder import *
from dag_eval import *


grmat, topo, pi = generateAddder(1)

print topo
for rows in grmat:
    mystring = ''
    for nodes in rows:
        if(nodes == -1):
            mystring = mystring + '.' + ' '
        else:
            mystring = mystring + str(nodes) + ' '
    print(mystring)

output, nv = dag_eval(grmat, topo, [1,1])

print output
print nv
'''


import utils.decbin as decbin
x = decbin.dec2bin(5, 5)
y = decbin.bin2dec(x)
print x
print y
