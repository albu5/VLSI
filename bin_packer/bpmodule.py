# Author: Sagun Pai (Famguy)
# Codename: Hello from the outside!
# Timestamp: 29th Oct 2015, 4:24 AM
# Location: Room no 325, Hostel 9, IIT Bombay, Powai
from copy import deepcopy

# given input dag_graph, we shall use the bin backing approach to get LUTs of specific size (5 in this case)
# dag for encoder

_GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}


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
	topo = []

	for ind, i in enumerate(dag_graph):
		j = onlygates(i)
		for gate in ['and', 'or']:
			numand = j.count(_GATE[gate])

			if numand > ls:
				newnod = original_size - 1
				nnumand = int(numand/f) # consecutive and gates
				rnumand = numand%f		# extra inputs in first one
				gatesadded = nnumand

				if rnumand == 0:
					rnumand = f

				for g in range(gatesadded):
					dag_graph = extenddag(dag_graph,-1)

				indexes = [k for k,x in enumerate(i) if x == _GATE[gate]]
				
				for nog in range(rnumand):
					indexes.pop(0)

				# setting only reminder number of gates in that level
				for u in indexes:
					dag_graph[ind][u] = -1

				dag_graph[ind][original_size] = _GATE[gate]

				for h in range(nnumand):
					if h+original_size not in topo:
						topo.append(h+original_size)
					for ul in range(f):
						try:
							inp1 = indexes.pop(0)
							dag_graph[h+original_size][inp1] = _GATE[gate]
						except Exception, e:
							pass

				for il in range(original_size,original_size+gatesadded+1):
					try:
						dag_graph[il][il+1] = _GATE[gate]
						if il+1 not in topo:
							topo.append(il+1)

					except Exception, e:
						pass
				original_size = len(dag_graph)

		if ind not in topo:
			topo.append(ind)

	printgraph(dag_graph)
	print topo
	return dag_graph, topo


