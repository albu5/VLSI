# Author: Sagun Pai (Famguy)
# Codename: Hello from the outside!
# Timestamp: 29th Oct 2015, 4:24 AM
# Location: Room no 325, Hostel 9, IIT Bombay, Powai
from pprint import pprint
from copy import deepcopy

# given input dag_graph, we shall use the bin backing approach to get LUTs of specific size (5 in this case)
LUTsize = 5
dag_graph3 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, -1, -1, -1], [-1, -1, 4, 4, -1, -1, 4, 4, -1, -1, 4, 4, -1, -1, 4, 4, -1, -1, -1, -1], [-1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1]]

dag_graph5 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 4, -1, 4, -1, 4, -1, 4, -1, -1, -1], [-1, -1, 4, 4, -1, -1, 4, 4, -1, -1, -1], [-1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1]]

# 10
dag_graph1 = [[-1,2,2,2,2,2,2,2,2,2,2],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# 9
dag_graph2 = [[-1,2,2,2,2,2,2,2,2,2],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# 8
dag_graph4 = [[-1,2,2,2,2,2,2,2,2],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1]]


# dag for encoder

_GATE = {'0':0, '1':1, 'and':4, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}


def printgraph(ngraph):
	for rows in ngraph:
	    mystring = ''
	    for nodes in rows:
	        if(nodes == -1):
	            mystring = mystring + '.' + ' '
	        else:
	            mystring = mystring + str(nodes) + ' '
	    print(mystring)

def onlygates(l):
	return [x for x in l if x not in [-1,0,1]]

def extenddag(dag,adds):
	dag_ret = deepcopy(dag)
	for k in dag_ret:
		k.append(adds)
	dag_ret.append([adds for s in range(len(k))])
	return dag_ret

def decompose(dag_graph, ls):
	original_size = len(dag_graph)
	f = ls - 1 

	for ind, i in enumerate(dag_graph):
		j = onlygates(i)
		numand = j.count(_GATE['and'])

		if numand > ls:
			# print i
			newnod = original_size - 1
			nnumand = int(numand/f) # consecutive and gates
			rnumand = numand%f		# extra inputs in first one
			gatesadded = nnumand

			if rnumand == 0:
				rnumand = f

			for g in range(gatesadded):
				dag_graph = extenddag(dag_graph,-1)
				#print "yo"

			indexes = [k for k,x in enumerate(i) if x == _GATE['and']]
			
			for nog in range(rnumand):
				indexes.pop(0)

			# setting only reminder number of gates in that level
			for u in indexes:
				dag_graph[ind][u] = -1

			dag_graph[ind][original_size] = _GATE['and']

			for h in range(nnumand):
				for ul in range(f):
					try:
						inp1 = indexes.pop(0)
						dag_graph[h+original_size][inp1] = _GATE['and']
					except Exception, e:
						pass

			for il in range(original_size,original_size+gatesadded+1):
				try:
					dag_graph[il][il+1] = _GATE['and']
				except Exception, e:
					pass
			original_size = len(dag_graph)
			# print rnumand
			# printgraph(dag_graph)


	printgraph(dag_graph)


printgraph(dag_graph5)
print "--------------------"
decompose(dag_graph5, 3)


